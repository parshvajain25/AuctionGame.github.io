import React from 'react';

class Card extends React.Component {
  render() {
    const img = this.props.img;
    const name = this.props.name;
    return (
      <div className="col-sm-6 col-md-4 col-lg-2">
        <div className="card gallery-item">
          <img className="card-img-top" src={img} alt={name} />
          <div className="card-body">
            <h5 className="card-title">{name}</h5>
            <button className="btn btn-primary">Predict</button>

            {/* add on click to this button  */}
          </div>
        </div>
      </div>
    );
  }
}

export default Card;
