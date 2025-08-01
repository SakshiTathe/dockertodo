### 🔹 1. **Install Prerequisites**
* **Node.js + npm** → [Download](https://nodejs.org/)
* **MongoDB** → [Download](https://www.mongodb.com/try/download/community)
### 🔹 2. **Start MongoDB**
* If MongoDB is installed locally, run it:
```bash
mongod
```
This will run MongoDB on `mongodb://localhost:27017`.
---
### 🔹 3. **Run Backend Locally**

#### a. Navigate to the backend folder:

```bash
cd backend
```

#### b. Install dependencies:

```bash
npm install
```
#### c. Start the backend:

```bash
npm start
```
Now your backend should be running at:
👉 `http://localhost:5000`
---
### 🔹 4. **Run Frontend Locally**
#### a. Open new terminal & go to frontend folder:
```bash
cd ../frontend
```
#### b. Install dependencies:
```bash
npm install
```
#### c. Start the frontend:
```bash
npm start
```
This will launch the frontend at:
👉 `http://localhost:3000`
---
---
| Component | Command                                       |
| --------- | --------------------------------------------- |
| MongoDB   | `mongod`                                      |
| Backend   | `npm install && npm start` inside `backend/`  |
| Frontend  | `npm install && npm start` inside `frontend/` |

---
