import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/board" element={<List />} />
        <Route path="/board/:문자열" element={<Detail />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;