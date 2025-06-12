import React, {useState} from 'react';
export const IntegrationsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>INTEGRATIONS - Integrations - TMS, WMS, ELD, telematics</h2><p>TMS</p></div>
};
export default IntegrationsView;
