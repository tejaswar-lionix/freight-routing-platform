import React, {useState} from 'react';
export const ShipmentsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>SHIPMENTS - Shipments - orders, tracking, BOL, POD, </h2><p>FTL</p></div>
};
export default ShipmentsView;
