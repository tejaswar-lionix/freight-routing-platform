import React, {useState} from 'react';
export const TrackingView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>TRACKING - Tracking - GPS, ETA, events, geofence</h2><p>GPS</p></div>
};
export default TrackingView;
