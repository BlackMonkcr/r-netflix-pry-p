import React, { useEffect, useState } from 'react';
import './Player.css';
import back_arrow_icon from '../../assets/back_arrow_icon.png';
import { useParams, Link } from 'react-router-dom';

const Player = () => {
	const { id } = useParams();
	const [apiData, setApiData] = useState({
		title: '',
		description: '',
		release_date: '',
		type: '',
		url_content: '',
		url_cover: '',
	});

	useEffect(() => {
		var requestOptions = {
			method: 'GET',
			redirect: 'follow',
		};

		const getContent = async () => {
			const response = await fetch(
				`http://lb-netflix-prod-2027007516.us-east-1.elb.amazonaws.com:8004/content/${id}`,
				requestOptions
			);

			const data = await response.json();
			setApiData(data);

			console.log(data);
		}

		getContent();
	}, []);

	return (
		<div className='player'>
			<Link to='/'>
				<img src={back_arrow_icon} alt='' className='link'/>
			</Link>
			<iframe
				width='100%'
				height='100%'
				src={apiData.url_content}
				title={apiData.title}
				frameborder='0'
				allowFullScreen
				autoPlay  // Add the autoPlay attribute to enable autoplay
			></iframe>
			<div className='player-info'>
				<p>{apiData.release_date}</p>
				<p>{apiData.title}</p>
				<p>{apiData.type}</p>
			</div>
		</div>
	);
};

export default Player;
