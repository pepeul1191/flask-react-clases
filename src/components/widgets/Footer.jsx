import React, { Component } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import './NavBar.css';

class Footer extends Component {
    constructor(props) {
    super(props);
        // Estado inicial del componente
        this.state = { };
    }

    incrementarContador = () => {
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
    render() {
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
              <Form action="#" method="POST">
                <Form.Group className="mb-3" controlId="email">
                  <Form.Label>Correo Electrónico</Form.Label>
                  <Form.Control type="email" placeholder="Tu correo" required />
                </Form.Group>
                <Form.Group className="mb-3" controlId="mensaje">
                  <Form.Label>Mensaje</Form.Label>
                  <Form.Control as="textarea" rows={3} placeholder="Escribe tu mensaje" />
                </Form.Group>
                <Button type="submit" variant="primary" className="w-100">
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