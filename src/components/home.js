import React from 'react';
// import * as firebase from 'firebase';
import Predict from './predict';

class Home extends React.Component {

  render() {
    const round = this.props.round;
    
    if (round === 'prediction') {
      return <Predict />;
    } else {
      return <h1>Current Round {round}</h1>;
    }
  }
}

export default Home;
