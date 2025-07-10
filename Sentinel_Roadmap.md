# 🚀 Sentinel Development Roadmap

## ⚙️ Technical Stack: Hybrid Architecture

| Component      | Tech                        | Notes                        |
|----------------|-----------------------------|------------------------------|
| **LLM API**    | OpenAI GPT-4o               | Core agent reasoning & dialogue |
| **Embeddings** | OpenAI API / E5-base local  | Journal entry vectorization |
| **Memory**     | FAISS (self-hosted)         | Per-user vector storage & recall |
| **Backend**    | FastAPI + Docker            | Business logic, API endpoints |
| **Database**   | MongoDB                     | User metadata + journaling |
| **Deployment** | Azure VM (Ubuntu, Docker)   | Cost-effective + flexible infra |

---

## 🚀 Development Stages

### Stage 0: Concept Definition
- Define user roles: Companion, Observer, Reviewer
- Design conversational flows and interventions
- Establish moderation and escalation criteria
- Choose core user scenarios: journaling, daily check-in, reflective chat

### Stage 1: Local MVP Build
- Scaffold project using `starter.sh` + `uv`
- Create `FastAPI` app with:
  - `/chat`, `/journal`, `/mood`, `/history`
- Integrate OpenAI GPT-4o API for responses
- Implement embedding + FAISS memory layer
- Log user prompts and vector matches in MongoDB

### Stage 2: Dockerization & Local Validation
- Create Dockerfile + `docker-compose.yml`
- Enable `.env`-based config loading (API keys, ports)
- Run and test locally: journal entry → vector → LLM response → store

### Stage 3: Azure VM Deployment
- Provision B2ms Ubuntu VM with Bicep
- Install Docker, NGINX, certbot
- Deploy app with HTTPS
- Open public ports: 80/443 (web), 22 (SSH), internal MongoDB closed

### Stage 4: UI or Chatbot Integration
- Add minimal frontend:
  - Option A: React/Tailwind journal + chat UI
  - Option B: Telegram bot
- Auth with Firebase/Auth0
- Connect to `/chat` + `/journal` endpoints

### Stage 5: Memory Intelligence & Feedback
- Implement FAISS recall + summarization
- Daily reflection agent: detects patterns, recommends insights
- Observer agent: flags concerning patterns (e.g., “I want to disappear”)
- Add human-in-the-loop UI or notification (Slack, email, admin panel)

### Stage 6: Monitoring & Metrics
- Add PostHog or custom dashboard
- Log key metrics: engagement, sentiment, escalation events
- Alerting on flagged sessions (via email/Slack)

### Stage 7: Monetization & Readiness
- Set up Stripe for premium journaling features
- Offer tiers: basic companion vs. premium memory/insight
- Add ToS, privacy policy, onboarding flow