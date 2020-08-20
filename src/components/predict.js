import React from 'react';
import Card from './card';

class Predict extends React.Component {
  render() {
    const items = [];
    for (var i = 0; i < 60; i++) {
      items.push(
        <Card
          img="https://avatars2.githubusercontent.com/u/56354790"
          name="nhbh"
        />,
      );
    }

    return (
      <div id="prediction-gallery">
        <h2 className="center">Make your predictions</h2>
        <div className="container">
          <div className="row">{items}</div>
        </div>
      </div>
    );
  }
}

export default Predict;
