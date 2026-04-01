# 🚀 Azure-WebApp-CI-CD

A containerized Flask web application designed for deployment on Azure Web Apps with continuous integration and continuous deployment (CI/CD) pipelines.

## ✨ Features

- **Flask Web Framework**: Lightweight and modular web application framework
- **MongoDB Integration**: Database support using PyMongo
- **Containerized**: Docker-based deployment for consistent environments
- **Azure Ready**: Optimized for Azure Web App deployment
- **CI/CD Pipeline**: Automated build and deployment workflows

## 📁 Project Structure

```
Azure-WebApp-CI-CD/
├── Dockerfile              # Docker container configuration
├── requirements.txt        # Python dependencies
├── app/                    # Main application directory
│   ├── __init__.py         # Flask application factory
│   ├── routes.py           # Application routes and views
│   ├── static/             # Static assets (CSS, JS, images)
│   │   └── css/
│   │       └── style.css
│   └── templates/          # Jinja2 templates
│       ├── base.html
│       └── index.html
└── README.md              # This file
```

## 📋 Prerequisites

- Python 3.11+
- Docker (for containerized deployment)
- MongoDB instance (local or cloud)
- Azure account (for deployment)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/simar022/Azure-WebApp-CI-CD.git
   cd Azure-WebApp-CI-CD
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```
   MONGODB_URI=mongodb://localhost:27017/your_database
   # Add other environment variables as needed
   ```

## 🏃‍♂️ Local Development

1. **Run the application locally:**
   ```bash
   export FLASK_APP=app/__init__.py
   flask run
   ```
   Or using Python:
   ```bash
   python -m flask run
   ```

2. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

3. **API Endpoints:**
   - `GET /`: Home page
   - `GET /status`: Application status (JSON response)

## 🐳 Docker Deployment

1. **Build the Docker image:**
   ```bash
   docker build -t azure-webapp .
   ```

2. **Run the container locally:**
   ```bash
   docker run -p 5000:5000 azure-webapp
   ```

3. **Access the containerized application:**
   Open your browser and navigate to `http://localhost:5000`

## ☁️ Azure Web App Deployment

1. **Create an Azure Web App:**
   - Go to the Azure Portal
   - Create a new Web App with Docker container support
   - Configure the deployment source (GitHub for CI/CD)

2. **Configure environment variables:**
   - In Azure Web App settings, add your MongoDB connection string and other secrets

3. **Deploy:**
   - Push changes to the main branch
   - Azure DevOps or GitHub Actions will automatically build and deploy

## 🔄 CI/CD Pipeline

This project includes automated CI/CD pipelines that:
- Run tests on each push
- Build Docker images
- Deploy to Azure Web Apps on successful builds

## ⚙️ Configuration

### 🔧 Environment Variables

- `MONGODB_URI`: MongoDB connection string
- `FLASK_ENV`: Set to `development` or `production`

### 🗄️ Database Setup

The application uses MongoDB. Ensure you have:
- A MongoDB instance running
- Proper connection string configured
- Database permissions set up

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### ⚠️ Common Issues

1. **Port already in use:**
   - Change the port in `app/__init__.py` or use a different port when running

2. **MongoDB connection errors:**
   - Verify your MongoDB URI is correct
   - Ensure MongoDB is running and accessible

3. **Docker build failures:**
   - Check that all dependencies are listed in `requirements.txt`
   - Ensure the Dockerfile is in the correct directory

### 📝 Logs

- Application logs are available in the Azure Web App logs
- For local development, check the terminal output

## 💬 Support

For support, please open an issue on the GitHub repository.