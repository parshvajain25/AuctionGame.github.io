import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import * as firebase from 'firebase';

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: 'AIzaSyAy8oi_BHmxutKBvJ2oQLaU41RB1m0qElc',
  authDomain: 'iit-auction.firebaseapp.com',
  databaseURL: 'https://iit-auction.firebaseio.com',
  projectId: 'iit-auction',
  storageBucket: 'iit-auction.appspot.com',
  messagingSenderId: '1009078682293',
  appId: '1:1009078682293:web:caafd6e69e15e62d29f4fc',
  measurementId: 'G-H7K3QDLHPQ',
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
