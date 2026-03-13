# 🌍 Wanderly - AI-Powered Travel Planning Platform

**Smart travel planning made simple**

Built with Python Flask + Groq AI (Llama 3.1 70B)

---

## 📁 Project Structure

```
wanderly/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment config
├── static/
│   └── index.html        # Frontend (get from Colab)
└── README.md             # This file
```

---

## 🚀 Quick Deploy (3 Steps)

### 1️⃣ Prepare Files

You need these 4 files:

✅ `app.py` - Already created!
✅ `requirements.txt` - Already created!
✅ `vercel.json` - Already created!
❗ `static/index.html` - **Copy from your Colab notebook**

### 2️⃣ Upload to GitHub

1. Create repository at https://github.com/new
2. Name it: `wanderly`
3. Upload all 4 files
4. Done!

### 3️⃣ Deploy to Vercel

1. Go to https://vercel.com/
2. Sign in with GitHub
3. Import your `wanderly` repo
4. Add environment variable:
   - Name: `GROQ_API_KEY`
   - Value: Your Groq API key
5. Deploy!

**You're live! 🎉**

---

## 🔑 Environment Variables

Set these in Vercel dashboard:

| Variable | Value | Required |
|----------|-------|----------|
| `GROQ_API_KEY` | Your Groq API key | ✅ Yes |

**Get Groq API key:** https://console.groq.com/

---

## 💡 Features

- ✨ Beautiful gradient landing page (Orange → Blue)
- 📝 Comprehensive trip planning form
- 🤖 AI-powered recommendations using Llama 3.1 70B
- 🏨 Smart budget allocation for hotels, food, transport
- 🚇 Complete transport info (Metro, Bike, Car, Taxi, Bus)
- 🍽️ Restaurant recommendations with cuisines
- 🎯 Attraction listings with costs
- 📅 Day-by-day itineraries with timeline
- 📱 Responsive design (mobile-friendly)
- 🏠 Home button for easy navigation

---

## 🛠️ Tech Stack

**Backend:**
- Python 3.10+
- Flask (web framework)
- Groq API (AI/LLM)
- Flask-CORS (API access)

**Frontend:**
- HTML5
- CSS3 (Gradients, Flexbox, Grid)
- Vanilla JavaScript
- Modern UI/UX design

**Deployment:**
- Vercel (hosting)
- GitHub (version control)

---

## 💰 Costs

| Service | Cost | Notes |
|---------|------|-------|
| Vercel | **FREE** | Unlimited personal projects |
| Groq API | **FREE** | No credit card required |
| GitHub | **FREE** | Public repositories |
| **Total** | **₹0/month** | 100% Free! |

---

## 🧪 Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variable:**
   ```bash
   export GROQ_API_KEY="your_key_here"
   ```

3. **Run server:**
   ```bash
   python app.py
   ```

4. **Open browser:**
   ```
   http://localhost:5000
   ```

---

## 📝 API Endpoints

### `GET /`
Returns the main page (index.html)

### `POST /api/plan`
Generate travel plan

**Request:**
```json
{
  "city": "Paris",
  "country": "France",
  "budget": 50000,
  "days": 5,
  "travelers": 2,
  "style": "balanced"
}
```

**Response:**
```json
{
  "city": "Paris",
  "hotels": [...],
  "restaurants": [...],
  "attractions": [...],
  "transport": {...},
  "itinerary": [...]
}
```

### `GET /api/test`
Health check endpoint

---

## 🎨 Design System

**Colors:**
- Primary: `#FF9F68` (Sand Orange)
- Secondary: `#A2D9FF` (Sky Blue)
- Background: `#F8F9FA` (Light Gray)
- Text: `#333333` (Dark Charcoal)

**Gradients:**
- Landing: `linear-gradient(135deg, #FF9F68, #A2D9FF)`
- Form/Results: `linear-gradient(to bottom, #FFF5F0, #E6F7FF)`

---

## 🔄 Update Deployment

When you make changes:

1. **Edit files** on GitHub
2. **Commit changes**
3. **Vercel auto-deploys** (1-2 minutes)
4. **Changes live!**

---

## 🐛 Troubleshooting

### Build Failed
- Check `requirements.txt` syntax
- Verify `app.py` has no errors
- Ensure all files are uploaded

### Application Error
- **Set `GROQ_API_KEY` in Vercel!** (most common issue)
- Check Vercel function logs
- Verify API key is valid

### API Not Working
- Confirm environment variable is set
- Check Groq API status
- Review browser console for errors

---

## 📚 Documentation

- **Vercel Docs:** https://vercel.com/docs
- **Flask Docs:** https://flask.palletsprojects.com/
- **Groq Docs:** https://console.groq.com/docs

---

## 👥 Team

- Arnav Mishra (22EJIAI008)
- Aryan Rajpurohit (22EJIAI009)
- Avneet Pal (22EJIAI014)

**Guide:** Mr. Krishan Pal Singh
**Institution:** JIET Group of Institutions, Jodhpur

---

## 📄 License

Educational Project - JIET 2025-26

---

## 🎉 Live Demo

**URL:** `https://wanderly-xyz.vercel.app`
(Replace xyz with your actual deployment ID)

---

**Built with ❤️ for travelers everywhere** 🌍✈️
