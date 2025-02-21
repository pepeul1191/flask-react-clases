import React, { Component } from 'react';
import { Card } from 'react-bootstrap';
import './Comment.css';

class Comment extends Component {
  constructor(props) {
    super(props);
    // Estado inicial del componente
    console.log(props);
    this.state = { };
  }
  // Método del ciclo de vida que se ejecuta después de que el componente se monta
  componentDidMount() {
    console.log('Componente montado');
    document.title = 'Ingresar a la Aplicación';
  }
  // Método del ciclo de vida que se ejecuta justo antes de que el componente se desmonte
  componentWillUnmount() {
    console.log('Componente a punto de desmontarse');
  }
  render() {
    const { comment, date, guest } = this.props;
    return (
      <Card>
        <Card.Body>
          <Card.Title>{comment}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted comment-date">{date}</Card.Subtitle>
          <Card.Text>{guest}</Card.Text>
        </Card.Body>
      </Card>
    );
  }
}
export default Comment;
