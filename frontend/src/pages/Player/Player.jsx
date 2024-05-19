import React, { useEffect, useState } from 'react';
import './Player.css';
import back_arrow_icon from '../../assets/back_arrow_icon.png';
import { useParams, Link } from 'react-router-dom';

const Player = () => {
	const { id } = useParams();
	const [apiData, setApiData] = useState({
		name: '',
		key: '',
		published_at: '',
		type: '',
	});

	useEffect(() => {
		var requestOptions = {
			method: 'GET',
			redirect: 'follow',
		};

		const getContent = async () => {
			const response = await fetch(
				`http://ec2-52-90-60-133.compute-1.amazonaws.com:8004/content/${id}`,
				requestOptions
			);

			const data = await response.json();
			setApiData(data.results);

			console.log(data.results);
		}

		getContent();
	}, []);

	return (
		<div className='player'>
			<Link to='/'>
				<img src={back_arrow_icon} alt='' />
			</Link>
			<iframe
				width='90%'
				height='90%'
				src={`https://www.youtube.com/embed/${apiData.key}`}
				title='trailer'
				frameborder='0'
				allowFullScreen
			></iframe>
			<div className='player-info'>
				<p>{apiData.published_at.slice(0, 10)}</p>
				<p>{apiData.name}</p>
				<p>{apiData.type}</p>
			</div>
		</div>
	);
};

export default Player;
