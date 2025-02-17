import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Container, Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './Web.css';
import HomePage from '../pages/web/HomePage.jsx';

const Web = () => {
  return (
    <Router>
      <Navbar bg="dark" variant="dark" expand="lg" sticky="top">
        <Container>
          <Navbar.Brand as={Link} to="/">React-Bootstrap</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link as={Link} to="/">Inicio</Nav.Link>
              <Nav.Link as={Link} to="/about">Nosotros</Nav.Link>
              <Nav.Link as={Link} to="/contact">Contacto</Nav.Link>
            </Nav>
          </Navbar.Collapse>
          <Nav className="ms-auto">
            <a href="/sign-in" className="nav-link">Iniciar Sesión</a> {/* HTML hyperlink */}
          </Nav>
        </Container>
      </Navbar>
      <Routes>
        <Route path="/" element={<HomePage />} />
      </Routes>
      <footer className="bg-dark text-white mt-5 p-4 text-center">
        Footer Content Here. © 2023 Company Name.
      </footer>
    </Router>
  );
};

export default Web