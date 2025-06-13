 For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCMke0Fhrum9hhCE_z4rYgrlguhu34G3HQ",
  authDomain: "heart-attack-prediction-d4873.firebaseapp.com",
  databaseURL: "https://heart-attack-prediction-d4873-default-rtdb.firebaseio.com",
  projectId: "heart-attack-prediction-d4873",
  storageBucket: "heart-attack-prediction-d4873.firebasestorage.app",
  messagingSenderId: "719482908255",
  appId: "1:719482908255:web:3f903933c5f94a85e775ea",
  measurementId: "G-FNDLB9EWYT"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
db.collection("users").add({
  name: "Jane Doe",
  email: "jane@example.com"
});
