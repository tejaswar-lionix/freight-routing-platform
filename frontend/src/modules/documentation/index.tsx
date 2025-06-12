import React, {useState} from 'react';
export const DocumentationView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>DOCUMENTATION - Documentation - BOL, POD, customs docs, </h2><p>BOL</p></div>
};
export default DocumentationView;
