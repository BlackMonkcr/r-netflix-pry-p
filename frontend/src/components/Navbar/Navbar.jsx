import React, { useEffect, useRef } from 'react';
import './Navbar.css';
import logo from '../../assets/logo.png';
import search_icon from '../../assets/search_icon.svg';
import bell_icon from '../../assets/bell_icon.svg';
import profile_img from '../../assets/profile_img.png';
import caret_icon from '../../assets/caret_icon.svg';
import { Link } from 'react-router-dom';

const Navbar = () => {
	const navRef = useRef();
	useEffect(() => {
		window.addEventListener('scroll', () => {
			if (window.scrollY >= 80) {
				navRef.current.classList.add('nav-dark');
			} else {
				navRef.current.classList.remove('nav-dark');
			}
		});
	}, []);
	return (
		<div ref={navRef} className='navbar'>
			<div className='navbar-left'>
				<img src={logo} alt='logo' />
				<ul>
					<li><Link to="/" className='link'>Inicio</Link></li>
					<li><Link to="/variado" className='link'>Variado</Link></li>
					<li><Link to="/peliculas" className='link'>Peliculas</Link></li>
					<li><Link to="/series" className='link'>Series</Link></li>
				</ul>
			</div>
			<div className='navbar-right'>
				<div className='navbar-profile'>
					<img src={profile_img} alt='profile image' className='profile' />
					<img src={caret_icon} alt='dropdown icon' className='' />
					<div className='dropdown'>
						<p
							onClick={() => {
								//logout();
							}}
						>
							Sign Out of Netflix
						</p>
					</div>
				</div>
			</div>
		</div>
	);
};

export default Navbar;
