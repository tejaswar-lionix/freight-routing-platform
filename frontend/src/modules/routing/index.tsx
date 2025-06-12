import React, {useState} from 'react';
export const RoutingView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>ROUTING - Routing - VRP, TSP, Dijkstra, A*, time w</h2><p>VRP</p></div>
};
export default RoutingView;
