import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for shipments, carriers, rout</h2><p>POST shipment</p></div>
};
export default ApiView;
