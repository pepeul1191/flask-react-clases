import React, { Component } from 'react';
import { Container, Row, Col, Form, Button, NavItem } from 'react-bootstrap';
import './InputText.css';

class InputText extends Component {
  constructor(props) {
    super(props);
    // Estado inicial del componente
    this.state = { 
      id: props.id || Math.random().toString(36).substring(2, 12),
      name: props.name,
      label: props.label,
      type: props.type || 'text', // text, email, ...
      className: props.className || '', 
      placeholder: props.placeholder || '',
      value: props.value || '', 
      valid: null,
      feedbackText: props.feedbackText /* {valid,invalid} */ || null, 
      disabled: props.disabled || false,
      onChangeValidations: props.onChangeValidations || [],
      onSubmitValidations: props.onSubmitValidations || [],
    };
    console.log(this.state)
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

  validateEmail = () => {
    const { value } = this.state;
    const regex = /^[a-zA-Z0-9._%+-]+@certus\.edu\.pe$/;
    if(value != ''){
      return regex.test(value);
    }else{
      return null;
    }
  }

  validateMaxLength = (maxLength) => {
    const { value } = this.state;
    if(value != ''){
      if(value.length <= maxLength){
        return true;
      }else{
        return false;
      }
    }else{
      return null;
    }
  }

  handleChange = (e) => {
    console.log(e.target)
    this.setState(
      {value: e.target.value}
    , () => {
      const {  onChangeValidations, valid, value } = this.state;
      var isValid = true;
      var feedbackText = '';
      onChangeValidations.forEach((validation) => {
        if(isValid){
          if(validation.type == 'email'){
            isValid = this.validateEmail();
          }else if(validation.type == 'maxLength'){
            isValid = this.validateMaxLength(validation.max);
          }
          feedbackText = isValid == null ? '' : (isValid ? validation.validText : validation.invalidTex);
        }
      });
      this.setState({valid: isValid});
      this.setState({feedbackText: feedbackText});
    });
  };

  render() {
    const { 
      id,
      name, 
      label, 
      type, 
      className, 
      valid, 
      feedbackText, 
      disabled, 
      placeholder,
      value,  
    } = this.state;
    return (
      <Form.Group className="mb-3" controlId="email">
        <Form.Label>{label}</Form.Label>
        <Form.Control 
          type={type}
          placeholder={placeholder} 
          value={value}
          name={name} 
          id={id}
          onChange={this.handleChange}
          className={`${className} ${valid == null ? "" : valid ? "is-valid" : "is-invalid"}`} 
          disabled={disabled}/>
        {valid == null ? '' :
          valid == true ?
            <Form.Control.Feedback>
              {feedbackText}
            </Form.Control.Feedback>:
            <Form.Control.Feedback type="invalid">  
              {feedbackText}
            </Form.Control.Feedback>}
      </Form.Group>
    );
  }
}

export default InputText;