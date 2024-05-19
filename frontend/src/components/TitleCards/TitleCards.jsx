import React, { useEffect, useRef, useState } from 'react';
import './TitleCards.css';
import { Link } from 'react-router-dom';

const TitleCards = ({ title, category }) => {
	const [apiData, setApiData] = useState([]);
	const cardsRef = useRef();

	const handleWheel = (event) => {
		event.preventDefault();
		cardsRef.current.scrollLeft += event.deltaY;
	};

	useEffect(() => {
		var requestOptions = {
			method: 'GET',
			redirect: 'follow',
		};

		const getContent = async () => {
			const response = await fetch(
				`http://ec2-52-90-60-133.compute-1.amazonaws.com:8004/content/`,
				requestOptions
			);

			const data = await response.json();
			setApiData(data.results);

			console.log(data.results);
		}

		getContent();
	}, []);

	// Divide las tarjetas en sublistas de 8 tarjetas cada una
	const chunkArray = (array, size) => {
		const chunkedArray = [];
		for (let i = 0; i < array.length; i += size) {
			chunkedArray.push(array.slice(i, i + size));
		}
		return chunkedArray;
	};

	const chunkedData = chunkArray(apiData, 8);

	return (
		<div className='title-cards'>
			<h2>{title ? title : 'Popular on Netflix'}</h2>
			{chunkedData.map((chunk, chunkIndex) => (
				<div className='card-list' ref={cardsRef} key={chunkIndex}>
					{chunk.map((card, index) => (
						<Link to={`/player/${card.id}`} className='card' key={index}>
							<img
								src={card.url_cover}
								alt='card image'
							/>
						</Link>
					))}
				</div>
			))}
		</div>
	);
};

export default TitleCards;
