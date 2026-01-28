import { get_playlists, get_recomendations, open_playlist } from './datagetter';
import {
  buildPlaylistsRecources,
  buildRecomendationRecource,
} from './dataformat';

// Playlists Button
const playlistsButton = document.getElementById('Playlists');
if (playlistsButton) {
  playlistsButton.addEventListener('click', loadPlaylists);
} else {
  console.error('Playlists button not found');
}

// Recomendations Button
const recomendationsButton = document.getElementById('Recomendations');
if (recomendationsButton) {
  recomendationsButton.addEventListener('click', loadRecomendations);
} else {
  console.error('Recomendations button not found');
}

// New Channel Button
const newChannelButton = document.getElementById('newChannelButton');
if (newChannelButton) {
  newChannelButton.addEventListener('click', addTopicChannel);
} else {
  console.error('New Channel button not found');
}

// Close Panel Button
const closePanelButton = document.getElementById('closePanelButton');
if (closePanelButton) {
  closePanelButton.addEventListener('click', closePanel);
} else {
  console.error('Close Panel button not found');
}

// TopicSwap Button
const topicSwapButton = document.getElementById('TopicSwap');
if (topicSwapButton) {
  topicSwapButton.addEventListener('click', openPanel);
} else {
  console.error('TopicSwap button not found');
}

function openPanel() {
  console.log('hello');
  document.getElementById('topicPanel').style.display = 'block';
}
function closePanel() {
  document.getElementById('topicPanel').style.display = 'none';
}
//? remove channel function()
//? brauche wohl db when ich das auch behalten will
//? eine funktionaliy tät die den neuen button auch etwas wie onclick added oder so?
function addTopicChannel() {
  let topicChannelName = prompt('Neuer Channel:');
  if (topicChannelName) {
    let item = document.createElement('li');
    let itemBut = document.createElement('button');
    itemBut.textContent = topicChannelName;
    itemBut.id = topicChannelName.slice(0, 8);
    document.getElementById('topicList').appendChild(item);
    document.getElementById('topicList').appendChild(itemBut);
  }
}

function loadRecomendations() {
  let recomendations = get_recomendations();
  let recomendationHTML = buildRecomendationRecource(recomendations);
  console.log(recomendationHTML);
}

function loadPlaylists() {
  let playlists = get_playlists();
  let playlistsHTML = buildPlaylistsRecources(playlists);
  console.log(playlistsHTML);
}

function openPlaylist(id) {
  console.log('hello world will build later');
}
