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
			<div className='hero'>
				<img src={hero_banner} alt='hero image' className='banner-img' />
				<div className='hero-caption'>
					<img src={hero_title} alt='hero title' className='caption-img' />
					<p>
					Un joven habitante de la moderna Estambul descubre sus lazos con una antigua orden secreta y se dispone a salvar a su ciudad de un enemigo inmortal.
					</p>
					<div className='hero-btns'>
						<button className='btn'>
							<img src={play_icon} alt='play icon img' />
							Play
						</button>
						<a href="https://www.netflix.com/pe/title/80189829">
							<button className='btn dark-btn' >
								<img src={info_icon} alt='info icon img' />
								More Info
							</button>
						</a>
					</div>
				</div>
			</div>
			<div className='more-cards'>
				<TitleCards title={'En Netflix hoy'} />
			</div>
			<Footer />
		</div>
	);
};

export default Home;
