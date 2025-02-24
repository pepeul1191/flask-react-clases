import React, { Component } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './Footer.css';

class Footer extends Component {
  constructor(props) {
    super(props);
    // Estado inicial del componente
    this.state = { 
      email: '', validEmail: null,
      message: '', validMessage: null, 
      disabled: true,
    };
  }

  validateEmail = () => {
    const { email } = this.state;
    if(email.length == 0){
      this.setState({validEmail: null});
    }else{
      const regex = /^[a-zA-Z0-9._%+-]+@certus\.edu\.pe$/;
      this.setState({validEmail: regex.test(email)});
    }
  };

  validateMessage = () => {
    const { message } = this.state;
    if(message.length == 0){
      this.setState({validMessage: null});
    }else{
      this.setState({validMessage: message.length > 0 && message.length <= 20});
    }
  };

  // Método del ciclo de vida que se ejecuta después de que el componente se monta
  componentDidMount() {
    console.log('Componente montado');
    document.title = 'Ingresar a la Aplicación';
  }
  // Método del ciclo de vida que se ejecuta justo antes de que el componente se desmonte
  componentWillUnmount() {
    console.log('Componente a punto de desmontarse');
  }
  handleChange = (e) => {
    this.setState(
      {[e.target.name]: e.target.value}
    , () => {
      if(e.target.name == 'message'){this.validateMessage()}
      if(e.target.name == 'email'){this.validateEmail()}
    });
  }

  handleSubmit = (e) => {
    e.preventDefault(); // Evitar que el formulario se recargue
    const { email, message } = this.state;
    const data = {
      email: email,
      message: message,
    }
    fetch('/api/message', {
      method: 'POST', // Método HTTP
      headers: {
          'Content-Type': 'application/json' // Indicar que se envía JSON
        },
        body: JSON.stringify(data) // Convertir el objeto a JSON
      })
      .then(response => {
        if (!response.ok) {
          throw new Error(`Error en la solicitud: ${response.status}`);
        }
        alert('Mensaje Enviado');
        this.setState({message: ''});
        this.setState({validMessage: null});
        this.setState({email: ''});        
        this.setState({validEmail: null});
      })
      .then(data => {
        console.log('Respuesta:', data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  render() {
    const { email, message, validEmail, validMessage} = this.state;
    return (
      <footer className="bg-dark text-white pt-5">
        <Container>
          <Row>
            {/* Secciones de la página */}
            <Col md={4} className="mb-4">
              <h5>Secciones</h5>
              <ul className="list-unstyled">
                <li><Link to="/" className="text-white text-decoration-none">Home</Link></li>
                <li><Link to="/nosotros" className="text-white text-decoration-none">Nosotros</Link></li>
                <li><Link to="/servicios" className="text-white text-decoration-none">Servicios</Link></li>
                <li><Link to="/clientes" className="text-white text-decoration-none">Clientes</Link></li>
                <li><Link to="/contacto" className="text-white text-decoration-none">Contacto</Link></li>
              </ul>
            </Col>

            {/* Información de contacto */}
            <Col md={4} className="mb-4">
              <h5>Contacto</h5>
              <p>
                📍 Dirección: Calle Principal, 123<br />
                📞 Teléfono: +1 234 567 890<br />
                📧 Email: contacto@vegüeta.com
              </p>
              <p>Síguenos en:</p>
              <a href="#" className="text-white me-3"><i className="bi bi-facebook"></i></a>
              <a href="#" className="text-white me-3"><i className="bi bi-twitter"></i></a>
              <a href="#" className="text-white"><i className="bi bi-instagram"></i></a>
            </Col>

            {/* Formulario */}
            <Col md={4} className="mb-4">
              <h5>Suscríbete</h5>
              <Form onSubmit={this.handleSubmit} method="POST">
                <Form.Group className="mb-3" controlId="email">
                  <Form.Label>Correo Electrónico</Form.Label>
                  <Form.Control 
                    type="email" 
                    placeholder="Tu correo" 
                    value={email}
                    name='email' 
                    onChange={this.handleChange}
                    className={validEmail == null ? "" : (validEmail ? 'is-valid' : 'is-invalid')}
                    required />
                    {validEmail == null ? "" : 
                      validEmail ?                       
                      <Form.Control.Feedback className={'valid-feedback'} type="valid">
                        Correo válido
                      </Form.Control.Feedback> :
                      <Form.Control.Feedback className={'invalid-feedback'} type="invalid">
                        Debe de ser un correo de Certus
                      </Form.Control.Feedback>
                    }
                </Form.Group>
                <Form.Group className="mb-3" controlId="mensaje">
                  <Form.Label>Mensaje ({message.length} / 20)</Form.Label>
                  <Form.Control 
                    as="textarea" 
                    rows={3} 
                    placeholder="Escribe tu mensaje" 
                    name='message' 
                    value={message}
                    onChange={this.handleChange}
                    className={validMessage == null ? "" : (validMessage ? 'is-valid' : 'is-invalid')}/>
                    {validMessage == null ? "" : 
                      validMessage ?                       
                      <Form.Control.Feedback className={'valid-feedback'} type="valid">
                        Mensaje válido
                      </Form.Control.Feedback> :
                      <Form.Control.Feedback className={'invalid-feedback'} type="invalid">
                        Mensaje no debe de superar los 20 caracteres.
                      </Form.Control.Feedback>
                    }
                </Form.Group>
                <Button 
                  type="submit" 
                  variant="primary" 
                  className="w-100" 
                  disabled={!validEmail || !validMessage}>
                  Enviar
                </Button>
              </Form>
            </Col>
          </Row>
        </Container>

        {/* Línea divisoria y derechos reservados */}
        <div className="text-center bg-secondary py-3 mt-4">
          <p className="mb-0">© 2025 Végueta. Todos los derechos reservados.</p>
        </div>
      </footer>  
    );
  }
}
export default Footer;