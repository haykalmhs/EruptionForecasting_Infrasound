from obspy import UTCDateTime
from waveform_collection import gather_waveforms, gather_waveforms_bulk
import obspy
from obspy.clients.fdsn.mass_downloader import Restrictions, MassDownloader
from obspy.clients.fdsn.mass_downloader.domain import CircularDomain

domain = CircularDomain(latitude= -7.540718, longitude= 110.445724,
                        minradius=0, maxradius=30.0)

restrictions = Restrictions(
    # Get data for a whole year.
    starttime=obspy.UTCDateTime(2018, 1, 1),
    endtime=obspy.UTCDateTime(2019, 1, 1),
    # Chunk it to have one file per day.
    chunklength_in_sec=86400,
    # Considering the enormous amount of data associated with continuous
    # requests, you might want to limit the data based on SEED identifiers.
    # If the location code is specified, the location priority list is not
    # used; the same is true for the channel argument and priority list.
    network="IM", location="", channel="*",
    # The typical use case for such a data set are noise correlations where
    # gaps are dealt with at a later stage.
    reject_channels_with_gaps=False,
    # Same is true with the minimum length. All data might be useful.
    minimum_length=0.0,
    # Guard against the same station having different names.
    minimum_interstation_distance_in_m=100.0)

# Restrict the number of providers if you know which serve the desired
# data. If in doubt just don't specify - then all providers will be
# queried.
mdl = MassDownloader(providers=["IRIS"])
mdl.download(domain, restrictions, mseed_storage="data", stationxml_storage="stations")