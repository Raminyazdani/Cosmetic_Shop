# Cosmetic Shop — Django Marketplace Template

A Django-based marketplace template for a cosmetics shop.

> **📋 See [REPORT.md](REPORT.md) for detailed setup audit, branch analysis, and verification results.**

This repo is organized as a multi-app Django project (products, users, shops, etc.) with a small “Core” framework that provides:

- **Reusable model fields** (`Core/fields/*`) via `Core.fields.ProjectFields`
- **Shared base models + soft-delete** (`Core.models.CoreModelUniversal` + `Core.managers.BaseManager`)
- **Model mixins** for common behavior (slug generation, `__str__`, save rules) under `Core/ProjectMixins/`
- A **custom management command** to scaffold apps and boilerplate mixins (`customstartapp`)

> Current UI entry point: `/` renders `templates/Shops/home.html` via `Shops.views.Home`.

---

## Tech stack

- Python (3.10+ recommended)
- Django 4.1.4
- Default database: SQLite (`db.sqlite3`)

---

## Project structure (high level)

- `Cosmetic_Shop/` — Django project (settings/urls/asgi/wsgi)
- `Core/` — shared framework utilities (fields, base models, mixins, generators)
- `Users/` — custom user model (`AUTH_USER_MODEL = 'Users.User'`)
- `Products/` — product catalog models (Product/Category/Brand/Tag/Comment + through models)
- `Shops/` — template-based pages (currently home)
- `Markets/`, `Costumers/`, `APIs/` — placeholder apps (present in `INSTALLED_APPS`, currently minimal models)
- `templates/` — global templates
- `statics/` — static assets (CSS/JS/Bootstrap)

---

## ✨ New Features (Integrated Branch Consolidation)

This repository has been consolidated from multiple branches to provide a complete e-commerce experience:

### 🛍️ Product Catalog
- **Product Listing** (`/products/`) - Browse all available products
- **Product Details** - View detailed product information
- **Search & Filters** - Find products by category, brand, or search term
- **Pagination** - Easy navigation through large catalogs

### 🛒 Shopping Cart
- **Add to Cart** - Add products from detail pages
- **Manage Cart** (`/cart/`) - View, update quantities, or remove items
- **Cart Summary** - Real-time total calculation
- **Persistent Cart** - Cart saved per user account

### 💳 Checkout & Orders
- **Checkout Process** (`/cart/checkout/`) - Complete order placement
- **Order Confirmation** - Success page after checkout
- **Order Models** - OrderItem, Payment, Shipment tracking
- **Admin Management** - Full order management in Django admin

### 👥 User Features
- **Authentication** - Login required for cart/checkout
- **Custom User Model** - Extended with phone, role flags
- **Admin Access** - Full Django admin panel

### 🎨 UI/UX
- **Responsive Design** - Bootstrap 5 templates
- **Navigation** - Consistent navbar across all pages
- **Messages** - User feedback for cart actions
- **Clean Layout** - Professional cosmetics shop appearance

---

## Apps & responsibilities

| App | What it’s for | Notes |
|---|---|---|
| `Core` | Base models, managers, reusable field definitions, mixins, code generators | `CoreModelUniversal` provides `id`, timestamps, and soft-delete fields. |
| `Users` | Custom user model | Extends `AbstractUser` and adds `phone_number`, flags like `is_costumer` / `is_market`, and a `slug`. |
| `Products` | Product catalog with views | Product/Category/Brand/Tag models + list/detail views with filtering/search |
| `Shops` | Shop models & pages | Order, OrderItem, Payment, Shipment, Address, Coupon, Discount models + home page |
| `Costumers` | Shopping cart & checkout | Cart, CartItem models + cart views + checkout flow |
| `Markets` | Marketplace seller-side (placeholder) | Reserved for future marketplace features |
| `APIs` | Future API endpoints (placeholder) | Not currently wired into root `urls.py`. |

---

## Key design concepts

### 1) Custom user model

This project sets:

- `AUTH_USER_MODEL = 'Users.User'`

The user model is defined in `Users/models.py` and adds a `phone_number` field plus role flags.

### 2) Centralized field definitions (`ProjectFields`)

You’ll see patterns like:

- `ProjectFields.CustomNameField(class_name="Product")`

Those field factories are aggregated in `Core/fields/ProjectFields.py` and implemented in the various modules inside `Core/fields/`.

This design keeps field options (verbose names, validators, indexes, defaults) centralized.

### 3) Base model + soft delete

Most domain models inherit from `Core.models.CoreModelUniversal`, which provides:

- `id`
- `created_at`, `modified_at`
- `is_delete` (soft-delete flag)
- `objects` / `subset` managers (`Core.managers.BaseManager`)

`BaseManager` includes helpers like:

- `get_deleted()`
- `restore()`
- `hard_delete()`

### 4) Mixins for behavior (slug/save/str)

Common behavior is implemented as mixins under `Core/ProjectMixins/`.
For example:

- `Core/ProjectMixins/Base/Save.py` contains save mixins like `SaveName` and `SaveId` (for slug generation)
- `Core/ProjectMixins/Base/Str.py` contains `__str__` mixins like `Name`, `ID`, etc.

---

## URL routing (request flow)

- Root URLConf: `Cosmetic_Shop/urls.py`
  - `/admin/` → Django Admin
  - `/` → `include('Shops.urls')`

- `Shops/urls.py`
  - `/` → `Shops.views.Home` (class-based view)

- `Shops/views.py`
  - Renders `templates/Shops/home.html`

---

## 🚀 Quick Start

To get the shop up and running with demo data:

1. **Setup:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Initialize Database:**
   ```bash
   python manage.py migrate
   python manage.py seed_demo
   ```

3. **Run Server:**
   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` to explore the shop.

---

## ✨ MVP Features (v1.0)

This project is now a fully functional MVP with the following features:

- **Auth:** Complete registration, login, and logout flows.
- **Catalog:** Browse products with category/brand filtering and search.
- **Cart:** Persistent shopping cart with add/remove/update capabilities.
- **Checkout:** Order creation flow with order item tracking and summary.
- **Admin:** Comprehensive admin panel for managing all entities.
- **Demo Data:** `seed_demo` command to instantly populate the catalog and users.
- **Tests:** Integrated test suite for core user journeys.

---

## 🛠️ Developer Tools

See [docs/RUNBOOK.md](docs/RUNBOOK.md) for detailed development instructions, credentials, and project structure.

---

## Static files & templates

- Templates live in:
  - `templates/` (project-level)
  - `*/templates/` (app-level, if present)

- Static assets live in `statics/` and are configured in `Cosmetic_Shop/settings.py`:
  - `STATICFILES_DIRS = [BASE_DIR / 'statics/']`
  - `STATIC_URL = 'statics/'`

> Note: Django convention is usually `STATIC_URL = '/static/'`. This project currently uses `statics/`.

---

## Custom scaffolding command: `customstartapp`

There’s a custom management command at:

- `Core/management/commands/customstartapp.py`

It wraps `startapp` and can also generate boilerplate for mixins and model scaffolding.

Examples:

```bash
# Create an app and generate scaffolding
python manage.py customstartapp --a MyApp --p Cosmetic_Shop --m ModelA ModelB --s SomeScopeParent --o soft

# Batch mode: read definitions from Core/management/AppMaker/making.txt
python manage.py customstartapp --o from --f making.txt
```

Options:

- `--o soft` (default): only add missing files/classes
- `--o hard`: overwrite
- `--o delete`: remove generated files
- `--o from`: batch create from a text file

---

## Database

Default database is SQLite:

- `db.sqlite3` in project root

To switch to Postgres/MySQL later, update the `DATABASES` setting.

---

## Admin

Django admin is enabled at `/admin/`.

If you customize admin registrations, you’ll do it in each app’s `admin.py`.

---

## Known config notes / quick checklist

These are worth reviewing before deploying:

- `SECRET_KEY` is hard-coded in `Cosmetic_Shop/settings.py` (move to environment variable for production)
- `DEBUG = True` (must be `False` in production)
- `ALLOWED_HOSTS` contains a likely typo: `"192,168.8.120"` (comma vs dot)
- No `MEDIA_ROOT` / `MEDIA_URL` configured yet (needed for user uploads)

---

## Tests

Automated tests aren’t implemented yet (each app has a `tests.py` placeholder).

To run Django tests:

```bash
python manage.py test
```

---

## License

See `LICENSE`.
