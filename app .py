# app.py - Wanderly Backend
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os
import json
import re

app = Flask(__name__, static_folder='static')
CORS(app)

# IMPORTANT: Get API key from environment variable (set in Vercel dashboard)
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

class TravelPlanner:
    def __init__(self):
        self.model = "llama-3.3-70b-versatile"
    
    def _call(self, prompt):
        """Call Groq API with error handling"""
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[{"role":"user","content":prompt}],
                max_tokens=3000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"API Error: {e}")
            return None
    
    def plan(self, city, country, budget_inr, days, people, style):
        """Generate travel plan based on user inputs"""
        
        # Budget allocation based on travel style
        alloc = {
            'budget': {'hotel':0.30,'food':0.30,'transport':0.25,'activities':0.10,'buffer':0.05},
            'balanced': {'hotel':0.35,'food':0.25,'transport':0.20,'activities':0.15,'buffer':0.05},
            'luxury': {'hotel':0.40,'food':0.25,'transport':0.15,'activities':0.15,'buffer':0.05}
        }[style]
        
        hotel_budget = int(budget_inr * alloc['hotel'])
        hotel_per_night = int(hotel_budget / days)
        food_per_day = int(budget_inr * alloc['food'] / days)
        
        # Create prompt for Groq API
        prompt = f"""Create a comprehensive {days}-day trip plan for {city}, {country}.

Budget Information:
- Total budget: ₹{budget_inr} for {people} travelers
- Trip duration: {days} days
- Hotel budget: ₹{hotel_per_night} per night MAXIMUM (very important!)
- Food budget: ₹{food_per_day} per day
- Travel style: {style}

Return ONLY valid JSON (no markdown, no code blocks, no explanations):
{{
  "hotels": [
    {{"name":"Hotel Name","address":"Full Address","price_inr":{hotel_per_night-500},"stars":3,"amenities":["WiFi","AC","Breakfast"]}}
  ],
  "restaurants": [
    {{"name":"Restaurant Name","cuisine":"Cuisine Type","price_range":"$$","specialty":"Signature Dish","avg_cost_inr":800}}
  ],
  "attractions": [
    {{"name":"Attraction Name","address":"Location","cost_inr":500,"duration":"2 hours","best_time":"Morning"}}
  ],
  "transport": {{
    "metro":{{"available":true,"day_pass_inr":400,"lines":["Line 1","Line 4"]}},
    "bike":{{"available":true,"cost_per_day_inr":300,"company":"Local Bike Rental"}},
    "car":{{"available":true,"cost_per_day_inr":2500}},
    "taxi":{{"available":true,"avg_cost_inr":500}},
    "bus":{{"available":true,"cost_per_ride_inr":50}}
  }},
  "itinerary": [
    {{
      "day":1,
      "morning":{{"activity":"Visit famous landmark","transport":"Metro Line 1"}},
      "lunch":{{"restaurant":"Restaurant name","cost_inr":800}},
      "afternoon":{{"activity":"Museum visit","transport":"Walk"}},
      "dinner":{{"restaurant":"Dinner spot","cost_inr":1200}}
    }}
  ]
}}

Requirements:
- Generate exactly 3 hotels (all priced ≤₹{hotel_per_night} per night)
- Generate 6 restaurants with varied cuisines
- Generate 5 attractions with entry costs and visit duration
- Generate complete {days}-day itinerary with specific activities
- Include realistic transport options for {city}
- All prices in INR (₹)"""
        
        # Call API
        content = self._call(prompt)
        if not content:
            return self._fallback(city, hotel_per_night)
        
        try:
            # Clean the response (remove markdown if present)
            content = content.replace('```json','').replace('```','').strip()
            
            # Extract JSON
            match = re.search(r'\{.*\}', content, re.DOTALL)
            if match:
                plan = json.loads(match.group())
                
                # Validate and fix hotel prices (critical!)
                for h in plan.get('hotels',[]):
                    if h.get('price_inr',99999) > hotel_per_night:
                        h['price_inr'] = hotel_per_night - 500
                
                print(f"✅ Successfully generated plan for {city}")
                return plan
        except Exception as e:
            print(f"Parse error: {e}")
        
        # If anything fails, return fallback
        return self._fallback(city, hotel_per_night)
    
    def _fallback(self, city, price):
        """Fallback plan if API fails"""
        return {
            "hotels":[{
                "name":f"Hotel in {city}",
                "address":"City Center",
                "price_inr":price-500,
                "stars":3,
                "amenities":["WiFi","AC"]
            }],
            "restaurants":[],
            "attractions":[],
            "transport":{"taxi":{"available":True,"avg_cost_inr":500}},
            "itinerary":[]
        }

# Initialize planner
planner = TravelPlanner()

@app.route('/')
def index():
    """Serve the main page"""
    return send_from_directory('static', 'index.html')

@app.route('/api/plan', methods=['POST'])
def plan_api():
    """API endpoint for generating travel plans"""
    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error":"No data provided"}), 400
        
        # Extract parameters
        city = data.get('city','')
        country = data.get('country','')
        budget = int(data.get('budget',10000))
        days = int(data.get('days',5))
        people = int(data.get('travelers',2))
        style = data.get('style','balanced')
        
        # Validate required fields
        if not city:
            return jsonify({"error":"City is required"}), 400
        
        print(f"📍 Planning trip to {city}, {country}")
        print(f"💰 Budget: ₹{budget} | Days: {days} | Travelers: {people} | Style: {style}")
        
        # Generate plan
        plan = planner.plan(city, country, budget, days, people, style)
        
        # Return structured response
        return jsonify({
            'city': city,
            'country': country,
            'days': days,
            'travelers': people,
            'budget': budget,
            'style': style,
            'hotels': plan.get('hotels',[]),
            'restaurants': plan.get('restaurants',[]),
            'attractions': plan.get('attractions',[]),
            'transport': plan.get('transport',{}),
            'itinerary': plan.get('itinerary',[])
        }), 200
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error":str(e)}), 500

@app.route('/api/test')
def test():
    """Test endpoint to verify API is working"""
    return jsonify({
        "status":"ok",
        "message":"Wanderly API is running!",
        "groq_configured": bool(os.environ.get('GROQ_API_KEY'))
    })

if __name__ == '__main__':
    # Get port from environment (Vercel sets this)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
