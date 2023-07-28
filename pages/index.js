import Head from 'next/head';
import styles from '../styles/Home.module.css';
import MyComponent from '../src/components/MyComponent';
import RecordComponent from '../src/components/RecordComponent';

export default function Home() {
 return (
  <div>
   <MyComponent />
   <RecordComponent />
  </div>
 );
}
