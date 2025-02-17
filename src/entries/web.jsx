import { createRoot } from 'react-dom/client';
import Web from '../components/layouts/Web.jsx';
import '../assets/stylesheets/styles.css';
import 'bootstrap/dist/css/bootstrap.min.css';

createRoot(document.getElementById('root')).render(
  <>
    <Web />
  </>,
)
