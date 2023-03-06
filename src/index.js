import React, { useEffect } from 'react';
import ReactDOM from 'react-dom';
import { Helmet } from 'react-helmet';

import './index.css';

import data from './just-custom-emojis-and-popularity.json';
data.sort(function(a, b) {
  return b.count - a.count;
});
data = data.slice(0, 6-1);

function A1() {
  console.log(data);
  return (
      <ul>
      {data.map((item, index) => (
        <li key={index}>
          <img src={item.url} alt={item.name} class="A1" />
        </li>
      ))}
    </ul>
  )
}

function A2() {
  console.log(data);
  return (
    <pre>
      {JSON.stringify(data, null, 2)};
    </pre>
  )
}

function TitleBar() {
  return (
    <div class="title-bar">
      <div class="title-bar-text">🔎 Emoji Search App</div>
    </div>
  )
}

function Grid() {
  return (
    <div class="grid-container">
      {data.map((item, index) => (
        <img src={item.emoji_url} alt={item.emoji_name} />
      ))}
    </div>
  )
}

function Head() {
  return (
    <Helmet>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous" />
    </Helmet>
  );
}

function Bootstrap() {
  return <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
}


ReactDOM.render(
  <React.StrictMode>
    <Head />
    <Bootstrap />
    <TitleBar />
    <div class="page-body">
      {/* <A1 /> */}
      {/* <A2 /> */}
      <Grid />
    </div>
  </React.StrictMode>,
  document.getElementById('root')
);