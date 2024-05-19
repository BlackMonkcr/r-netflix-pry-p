import React, { useEffect } from 'react';
import Home from './pages/Home/Home';
import Variado from './pages/Home/Variado';
import Peliculas from './pages/Home/Peliculas';
import Series from './pages/Home/Series';
import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from './pages/Login/Login';
import Player from './pages/Player/Player';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const App = () => {
	const navigate = useNavigate();
	useEffect(() => {
	}, []);
	return (
		<div>
			<ToastContainer theme='dark' />
			<Routes>
				<Route path='/' element={<Home />} />
				<Route path='/variado' element={<Variado />} />
				<Route path='/peliculas' element={<Peliculas />} />
				<Route path='/series' element={<Series />} />
				<Route path='/login' element={<Login />} />
				<Route path='/player/:id' element={<Player />} />
			</Routes>
		</div>
	);
};

export default App;
