import React from 'react';
import './index.css';

function App(){
  return (
    <div className='min-h-screen bg-gray-50'>
      <nav className='bg-white shadow'>
        <div className='max-w-6xl mx-auto px-4 py-4'>
          <span className='text-xl font-semibold'>CivicStack</span>
        </div>
      </nav>
      <main className='max-w-6xl mx-auto p-6'>
        <h1 className='text-3xl font-bold'>CivicStack — Open civic reporting</h1>
        <p className='mt-4 text-gray-600'>Report local issues with location and a photo. This repo is open-source and will be developed through March for FOSS Hack 2026.</p>
        <div className='mt-8'>
          <a className='inline-block bg-blue-600 text-white px-4 py-2 rounded' href='https://github.com/YOUR-GITHUB-USERNAME/civicstack'>View Repo</a>
        </div>
      </main>
    </div>
  );
}

export default App;
