import React, { useState } from 'react';
import './Login.css';
import logo from '../../assets/logo.png';
import netflix_spinner from '../../assets/netflix_spinner.gif';

const Login = () => {
	const [signState, setSignState] = useState('Sign In');
	const [name, setName] = useState('');
	const [email, setEmail] = useState('');
	const [password, setPassword] = useState('');
	const [loading, setLoading] = useState(false);

	const login = async (email, password) => {
		console.log(email, password);
		try {
			var myHeaders = new Headers();
			myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
			
			var urlencoded = new URLSearchParams();
			urlencoded.append("username", email);
			urlencoded.append("password", password);
			
			var requestOptions = {
				method: 'POST',
				headers: myHeaders,
				body: urlencoded,
				redirect: 'follow'
			};

			const response = await fetch('http://lb-netflix-prod-2027007516.us-east-1.elb.amazonaws.com:8000/token/', requestOptions);
			const data = await response.json();
			var myHeaders = new Headers();
			myHeaders.append("Authorization", `Bearer ${data.access_token}`);

			var requestOptions = {
				method: 'GET',
				headers: myHeaders,
				redirect: 'follow'
			};

			const response_2 = await fetch("http://lb-netflix-prod-2027007516.us-east-1.elb.amazonaws.com:8000/users/me", requestOptions);
			const data_2 = await response_2.json();
			localStorage.setItem('user', JSON.stringify(data_2));
			localStorage.setItem('token', data.access_token);
			window.location.href = '/';
		}
		catch (error) {
			console.log(error);
		}
	};

	const signup = async (name, email, password) => {
		try {
			const response = await fetch(`http://lb-netflix-prod-2027007516.us-east-1.elb.amazonaws.com:8003/users?username=${name}&email=${email}&password=${password}`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
			})
			
			const data = await response.json();
			console.log(data);
		} catch (error) {
			console.log(error);
		}
	};

	const user_auth = async (event) => {
		event.preventDefault();
		setLoading(true);
		if (signState === 'Sign In') {
			await login(email, password);
		} else {
			await signup(name, email, password);
		}
		setLoading(false);
	};
	return loading ? (
		<div className='login-spinner'>
			<img src={netflix_spinner} alt='netflix spinner' />
		</div>
	) : (
		<div className='login'>
			<img src={logo} alt='logo' className='login-logo' />
			<div className='login-form'>
				<h1>{signState}</h1>
				<form>
					{signState === 'Sign Up' ? (
						<input
							value={name}
							onChange={(e) => {
								setName(e.target.value);
							}}
							type='text'
							placeholder='Your name'
						/>
					) : (
						<></>
					)}
					<input
						value={email}
						onChange={(e) => {
							setEmail(e.target.value);
						}}
						type='email'
						placeholder='Email'
					/>
					<input
						value={password}
						onChange={(e) => {
							setPassword(e.target.value);
						}}
						type='password'
						placeholder='Password'
					/>
					<button onClick={user_auth} type='submit'>
						{signState}
					</button>
					<div className='form-help'>
						<div className='remember'>
							<input type='checkbox' />
							<label htmlFor=''>Remember me</label>
						</div>
						<p>Need Help?</p>
					</div>
				</form>
				<div className='form-switch'>
					{signState === 'Sign In' ? (
						<p>
							New to Netflix?
							<span
								onClick={() => {
									setSignState('Sign Up');
								}}
							>
								Sign Up Now
							</span>
						</p>
					) : (
						<p>
							Already have account?
							<span
								onClick={() => {
									setSignState('Sign In');
								}}
							>
								Sign In Now
							</span>
						</p>
					)}
				</div>
			</div>
		</div>
	);
};

export default Login;
