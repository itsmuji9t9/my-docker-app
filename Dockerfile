# 1. Base image select karein jismein Python pehle se install ho
FROM python:3.10-slim

# 2. Container ke andar ek folder banayein jahan kaam hoga
WORKDIR /app

# 3. Apne computer se app.py file ko container ke andar copy karein
COPY app.py .

# 4. Container ka port 8080 open karein taake internet se traffic aa sake
EXPOSE 8080

# 5. Container start hote hi jo command chalani hai
CMD ["python", "app.py"]
