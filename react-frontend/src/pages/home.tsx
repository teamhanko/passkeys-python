import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen">
            <h1 className="text-2xl font-bold mb-4">Home</h1>
            <Link to="/login" className="px-4 py-2 bg-black text-white rounded-md transition duration-150 ease-in-out">Go to Login</Link>
        </div>
    );
}

export default Home;