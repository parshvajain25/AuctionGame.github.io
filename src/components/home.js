import React from 'react';
import * as firebase from 'firebase';
import Predict from './predict';

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      round: '...',
    };
  }

  updateRound(round) {
    this.setState({
      round: round,
    });
  }

  // Add firebase updates and listener here
  componentDidMount() {
    const db = firebase.firestore();
    const doc = db.collection('admin').doc('current');

    doc.onSnapshot(
      (snap) => {
        console.log('Recieved pid', snap.data().pid);
        this.updateRound(snap.data().pid);
      },
      (err) => {
        console.log(`Encountered error: ${err}`);
      },
    );
  }

  render() {
    const round = this.state.round;
    if (round === 'prediction') {
      return <Predict />;
    } else {
      return <h1>Current Round {round}</h1>;
    }
  }
}

export default Home;
