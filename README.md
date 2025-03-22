# AI Code Reviewer 🤖

An intelligent code review system powered by Google's Gemini AI and deployed on AWS cloud infrastructure.

## 🌟 Features

- **AI-Powered Analysis**: Real-time code feedback using Gemini AI
- **Cloud-Native**: AWS deployment with containerized architecture
- **Interactive UI**: Rich code editor with syntax highlighting
- **Scalable**: Elastic Container Service with auto-scaling
- **Secure**: AWS security best practices and encrypted data storage

## 🛠️ Tech Stack

- **Frontend**: React.js, Monaco Editor
- **Backend**: Python Flask
- **Database**: PostgreSQL (AWS RDS)
- **Cloud**: AWS (ECS, ECR, RDS, ALB)
- **AI**: Google Gemini AI
- **Infrastructure**: Docker, Terraform

## 🚀 Quick Start

### Prerequisites

- Node.js 16+
- Python 3.9+
- Docker Desktop
- AWS CLI
- Google Gemini API key

### Local Development

1. **Clone repository**
```bash
git clone https://github.com/yourusername/ai-code-reviewer.git
cd ai-code-reviewer
```

2. **Set up environment variables**
Create `.env` file:
```properties
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_DB=ai_review
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/ai_review
GEMINI_API_KEY=your_gemini_api_key
```

3. **Start containers**
```bash
docker-compose up --build
```

## 🌩️ AWS Deployment

1. **Push to ECR**
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com
docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/ai-code-reviewer:latest
```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|---------|------------|
| `/api/analyze` | POST | Submit code for analysis |
| `/api/health` | GET | Service health check |

## 🔐 Security

- SSL/TLS encryption
- AWS WAF protection
- Secrets management
- VPC isolation
- Regular security patches

## 📊 Monitoring

- CloudWatch metrics
- ECS insights
- RDS monitoring
- Application logs

## 🤝 Contributing

1. Fork repository
2. Create feature branch
```bash
git checkout -b feature/amazing-feature
```
3. Commit changes
```bash
git commit -m 'Add amazing feature'
```
4. Push and create PR

## 📄 License

MIT License - see [LICENSE.md](LICENSE.md)

## 📞 Support

- Create GitHub issue
- Email: support@aicodereview.com
- Documentation: [docs/](docs/)

## ✅ Environment Variables

### Local Development
```properties
REACT_APP_API_URL=http://localhost:5000
POSTGRES_USER=postgres
POSTGRES_PASSWORD=local
```

### Production
```properties
REACT_APP_API_URL=https://api.aicodereview.com
DATABASE_URL=postgresql://${RDS_USER}:${RDS_PASS}@${RDS_ENDPOINT}:5432/ai_review
```

---
**Note**: Replace placeholder values before deployment.