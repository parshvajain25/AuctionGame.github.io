import React from 'react';
import Input from '@material-ui/core/Input';
import * as firebase from 'firebase';

class Quiz extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      userID: 'RPtYx30BJ0EuTzPuMQhI',
      currentQuestionNumber: 1,
      currentQuestion: '',
      answer: '',
      questions: {},
    };
    this.updateQuestion = this.updateQuestion.bind(this);
    this.handleAnswerInput = this.handleAnswerInput.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  updateQuestion(value) {
    this.setState({
      currentQuestion: value,
    });
  }

  handleAnswerInput(event) {
    this.setState({ answer: event.target.value });
  }

  handleSubmit(event) {
    var answer = this.state.answer;
    var Qno = this.state.currentQuestionNumber;
    event.preventDefault();

    var tempDict = {};
    tempDict[Qno] = answer;

    const db = firebase.firestore();
    db.collection('answers')
      .doc(this.state.userID)
      .set(tempDict, { merge: true });

    var newQno = this.state.currentQuestionNumber + 1;

    this.setState({
      answer: '',

      //we will change this later, there should be a prev next tab instead

      currentQuestion: this.state.questions[newQno],
      currentQuestionNumber: newQno,
    });
  }

  componentDidMount() {
    const db = firebase.firestore();
    const doc = db.collection('questions').doc('questionSet');

    doc
      .get()
      .then((doc) => {
        if (doc.exists) {
          console.log(doc.data());
          console.log(this.state.currentQuestion);

          this.setState({
            currentQuestion: doc.data()[this.state.currentQuestionNumber],
            questions: doc.data(),
          });
        } else {
          // doc.data() will be undefined in this case
          console.log('No such document!');
        }
      })
      .catch(function (error) {
        console.log('Error getting document:', error);
      });
  }

  render() {
    return (
      <div id="quiz-box" className="container">
        <div className="jumbotron">
          <h3 className="display-4">
            Question {this.state.currentQuestionNumber}
          </h3>
          <p className="lead">{this.state.currentQuestion}</p>
          <hr className="my-4" />
          <form onSubmit={this.handleSubmit}>
            <p>
              <Input
                onChange={this.handleAnswerInput}
                value={this.state.answer}
              ></Input>
            </p>
            <p className="lead">
              <button type="Submit" className="btn btn-primary">
                Submit
              </button>
            </p>
          </form>
        </div>
      </div>
    );
  }
}

export default Quiz;
