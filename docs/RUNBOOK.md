# Cosmetic Shop — Developer Runbook

This document provides instructions for common development operations.

## 🚀 Quick Start (Local Development)

1. **Setup Virtual Environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migration:**
   ```bash
   python manage.py migrate
   ```

4. **Seed Demo Data:**
   ```bash
   python manage.py seed_demo
   ```
   *This command creates an admin user, a customer user, and a sample product catalog.*

5. **Run Development Server:**
   ```bash
   python manage.py runserver
   ```

## 👤 Credentials (after seed_demo)

- **Admin User:**
  - Phone: `1234567890`
  - Password: `admin123`
- **Customer User:**
  - Phone: `0912345678`
  - Password: `customer123`

## 🧪 Testing

Run the full test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test Core
```

## 🛠️ Management Commands

- `seed_demo`: Populates the database with realistic sample data.
- `customstartapp`: Scaffolds a new Django app with Core framework mixins.
  ```bash
  python manage.py customstartapp --a MyApp --p Cosmetic_Shop --m ModelA ModelB
  ```

## 📂 Project Structure

- `Core/`: Shared utilities, base models, and mixins.
- `Users/`: Custom User model (`phone_number` as identifier).
- `Products/`: Product, Category, Brand, and Tag models.
- `Shops/`: Order, Payment, and Shop-related models.
- `Costumers/`: Shopping Cart and Checkout logic.
- `templates/`: Global and app-specific templates (Bootstrap 5).
- `statics/`: CSS, JS, and asset files.
