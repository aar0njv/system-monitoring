# System Monitoring Script 🖥️

## 📌 Overview
This is a simple **Python-based system monitoring script** that logs:
- CPU Usage
- Memory Usage
- Disk Usage
- Network Activity

The script runs every **10 seconds** and saves logs in a file.

---

##📌 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/system_monitoring.git
cd system_monitoring
```

### **2️⃣ Set Up Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # (For Windows: venv\Scripts\activate)
```

### **3️⃣ Install Dependencies**
```bash
pip install psutil
```

---

## 📌 Running the Script

### **Manual Execution**
```bash
python3 monitor.py
```
OR (if made executable)
```bash
./monitor.py
```

### **Check Logs**
```bash
cat logs/system_monitor.log
```

### **Run in Background**
```bash
nohup ./monitor.py &
```

---

## 📌 Automation with Cron Jobs

### **Run Every 10 Minutes**
```bash
crontab -e
```
Add this line:
```
*/10 * * * * /home/your_username/system_monitoring/monitor.py
```

### **Run on System Boot**
```bash
crontab -e
```
Add this line:
```
@reboot /home/your_username/system_monitoring/monitor.py
```

---

## 📌 Contributing
Feel free to fork this repository, make improvements, and submit pull requests! 🚀

## 📌 License
This project is open-source under the MIT License.

---

### **Author**
👤 [Aaron Joy]  
📧 aaronjoy382@gmail.com  
🔗 [GitHub Profile](https://github.com/aar0njv)


