import React from 'react';
import './Home.css';
import Navbar from '../../components/Navbar/Navbar';
import hero_banner from '../../assets/hero_banner.jpg';
import hero_title from '../../assets/hero_title.png';
import play_icon from '../../assets/play_icon.png';
import info_icon from '../../assets/info_icon.png';
import TitleCards from '../../components/TitleCards/TitleCards';
import Footer from '../../components/Footer/Footer';
import { useHref } from 'react-router-dom';

const Home = () => {
	return (
		<div className='home'>
			<Navbar />
			<div className='more-cards'>
				<TitleCards title={'Tus mejores Peliculas en Netflix'} category="pelicula"/>
			</div>
			<Footer />
		</div>
	);
};

export default Home;
