import React, {useState} from 'react';
export const OrdersView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>ORDERS - Orders - customers, quotes, rating, cont</h2><p>customers</p></div>
};
export default OrdersView;
