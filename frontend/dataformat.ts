import { get_playlists, get_recomendations, open_playlist } from './datagetter';

export function buildPlaylistsRecources(playlistdict: any) {
  console.log(playlistdict);
}
export function buildRecomendationRecource(videosdict: any) {
  console.log(videosdict);
  buildVideoResource(videosdict);
}

function buildVideoResource(videodata: any) {
  console.log(videodata);
  //! diese funktion braucht : src="https://www.youtube.com/embed/iaAHQPM1AOk", kannelbanner, videotitel, kanalname, videolänge
}

/*

<div class="mb-4 border-2 p-2 w-full md:w-1/2 lg:w-1/3" id="videoDiv"> //! this is the div in which the video goes 
          <iframe
            class="rounded-xl w-full"
            height="250"
            src="https://www.youtube.com/embed/iaAHQPM1AOk"
            frameborder="0"
            allow="
              accelerometer;
              clipboard-write;
              encrypted-media;
              gyroscope;
              picture-in-picture;
            "
            allowfullscreen
          ></iframe>
          <div class="flex items-start mt-2">
            <img
              src="https://yt3.ggpht.com/s92_ZA6Dc-TmMI1zSZFtGcXv4Rrsl3XeP8hE2HUc402u18pfsriNkWrkLtqXAfjIq1K9Zi5D2p8=s88-c-k-c0x00ffffff-no-rj"
              class="rounded-full w-12 h-12 object-cover mr-2"
              alt="Channel Banner"
            />
            <div>
              <h6 class="text-gray-50 w-80 break-words">
                JEDER CHUNK BESTEHT AUS EINEM BLOCK
              </h6>
              <div class="flex items-center">
                <h5 class="text-gray-50 mr-auto font-bold text-xl">BastiGHG</h5>
                <button
                  id="videoInterakt1"
                  class="text-gray-50 font-bold text-3xl focus:text-gray-300"
                >
                  :
                </button>
              </div>
              <h1 class="text-stone-200">14:40</h1>
            </div>
          </div>
        </div>

*/
