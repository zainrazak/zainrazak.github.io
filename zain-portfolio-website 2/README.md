# Zain Razak - Personal Portfolio Website

AI-Focused Product Manager Portfolio with integrated AI Chatbot

## 🚀 Project Structure

```
zain-portfolio-website/
├── index.html              # Homepage
├── experience.html         # Experience page (to be created)
├── certifications.html     # Certifications page (to be created)
├── projects.html           # Projects page (to be created)
├── interests.html          # Personal interests page (to be created)
├── css/
│   └── style.css          # Main stylesheet (AI Innovator theme)
├── js/
│   └── script.js          # Interactive features
├── chatbot/               # AI Career Chatbot
│   ├── app.py            # Simplified Gradio app
│   ├── models.py         # Chatbot models and functions
│   ├── career_chatbot.py # Main chatbot (alternative version)
│   ├── requirements.txt  # Python dependencies
│   ├── .env.template     # Environment variables template
│   ├── me/              # Personal data
│   │   ├── summary.txt
│   │   └── ZainLinkedinProfile.pdf
│   └── prompts/
│       └── chat_init.md  # System prompt
└── README.md             # This file
```

## 📋 Prerequisites

1. **GitHub Account** - Create at github.com/zainrazak
2. **OpenAI API Key** - Get from platform.openai.com
3. **Node.js** (optional) - For local testing
4. **Python 3.9+** - For running chatbot locally

## 🛠️ Setup Instructions

### Step 1: GitHub Setup

1. Create GitHub account at https://github.com (username: zainrazak)
2. Create a new repository: `zainrazak.github.io` (this enables GitHub Pages)
3. Upload all website files to this repository

### Step 2: Chatbot Setup (Local Testing)

1. Navigate to the chatbot directory:
```bash
cd chatbot
```

2. Create `.env` file from template:
```bash
cp .env.template .env
```

3. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
GITHUB_USERNAME=zainrazak
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

5. Run the chatbot locally:
```bash
python app.py
```

6. Open browser to `http://localhost:7860`

### Step 3: Deploy Chatbot to Hugging Face Spaces

1. Create account at https://huggingface.co/
2. Create new Space:
   - Name: `zainrazak-chatbot`
   - SDK: Gradio
   - Hardware: CPU (free tier)

3. Upload chatbot files to the Space:
   - app.py
   - models.py
   - requirements.txt
   - me/ folder (with your data files)
   - prompts/ folder

4. Add your OpenAI API key in Space Settings → Repository Secrets:
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key

5. Your chatbot will be live at: `https://huggingface.co/spaces/zainrazak/zainrazak-chatbot`

### Step 4: Embed Chatbot in Website

Add this to your projects.html page:

```html
<iframe
    src="https://huggingface.co/spaces/zainrazak/zainrazak-chatbot"
    frameborder="0"
    width="100%"
    height="800px"
></iframe>
```

### Step 5: Deploy Website

#### Option A: GitHub Pages (Recommended - FREE)

1. Push all files to your `zainrazak.github.io` repository
2. Go to Settings → Pages
3. Source: Deploy from main branch
4. Your site will be live at: `https://zainrazak.github.io`

#### Option B: Netlify (Alternative - FREE)

1. Create account at https://netlify.com
2. Connect your GitHub repository
3. Deploy settings:
   - Build command: (leave empty)
   - Publish directory: /
4. Add custom domain: zainrazak.com

### Step 6: Custom Domain Setup (zainrazak.com)

1. Purchase domain at Namecheap or Google Domains (~$12/year)
2. Add DNS records:

For GitHub Pages:
```
A Record: @ → 185.199.108.153
A Record: @ → 185.199.109.153
A Record: @ → 185.199.110.153
A Record: @ → 185.199.111.153
CNAME Record: www → zainrazak.github.io
```

For Netlify:
```
CNAME Record: @ → your-netlify-site.netlify.app
```

3. Add custom domain in GitHub/Netlify settings
4. Enable HTTPS (automatic with both platforms)

## 🎨 Design Theme

**AI Innovator Theme**
- Dark mode with purple/blue AI accents
- Animated gradient background
- Interactive elements
- Futuristic and modern aesthetic

## 📝 To-Do List

### Immediate Tasks:
- [ ] Create GitHub account and repository
- [ ] Get OpenAI API key
- [ ] Test chatbot locally
- [ ] Deploy chatbot to Hugging Face
- [ ] Create remaining HTML pages (experience, certifications, projects, interests)
- [ ] Deploy website to GitHub Pages
- [ ] Set up custom domain

### Future Enhancements:
- [ ] Add more AI agent projects
- [ ] Improve chatbot with RAG (Retrieval Augmented Generation)
- [ ] Add blog section for AI insights
- [ ] Implement dark/light mode toggle
- [ ] Add analytics (Google Analytics or Plausible)

## 🔧 Customization

### Update Colors:
Edit `css/style.css` and modify CSS variables:
```css
:root {
    --primary-color: #4F46E5;  /* Change this */
    --secondary-color: #7C3AED; /* And this */
}
```

### Update Content:
- Edit HTML files directly
- Modify `chatbot/me/summary.txt` for chatbot knowledge
- Update `chatbot/prompts/chat_init.md` for chatbot personality

## 📞 Support

If you encounter issues:
1. Check browser console for errors (F12)
2. Verify all file paths are correct
3. Ensure API keys are properly set
4. Check that all dependencies are installed

## 🎯 Next Steps After Setup

1. **Complete all pages** - Add content to experience, certifications, projects, interests
2. **Optimize chatbot** - Expand knowledge base, improve accuracy
3. **Build more AI projects** - Add to projects page
4. **Share your website** - Add to LinkedIn, resume, email signature
5. **Iterate and improve** - Gather feedback, make updates

## 📊 Performance Tips

- Optimize images (use WebP format, compress)
- Minimize CSS/JS (use minification tools)
- Enable caching
- Use CDN for static assets
- Monitor with Google PageSpeed Insights

## 🔐 Security Notes

- Never commit `.env` file to Git
- Keep API keys secret
- Use environment variables in production
- Regularly update dependencies

---

**Built with ❤️ by Zain Razak**

For questions or suggestions, reach out:
- Email: zainrazak007@gmail.com
- LinkedIn: https://www.linkedin.com/in/zainrazak/
- GitHub: https://github.com/zainrazak
