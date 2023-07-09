#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Hd Tx Hackrf
# GNU Radio version: 3.10.7.0-rc1

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import hd_tx_hackrf_epy_block_0 as epy_block_0  # embedded python block
import math
import nrsc5
import osmosdr
import time




class hd_tx_hackrf(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Hd Tx Hackrf", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.sig = sig = [0x40, 0x01, 0x00, 0x02, 0x69, 0x05, 0x00, 0x48, 0x44, 0x31, 0x66, 0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x5a, 0x6c, 0xc6, 0x4d, 0x67, 0x0d, 0x01, 0x00, 0x10, 0x09, 0x01, 0x03, 0x00, 0x00, 0x36, 0x75, 0x4b, 0xbe, 0x60, 0x09, 0x53, 0x45, 0x4c, 0x46, 0x28, 0x00, 0x00, 0x00, 0x67, 0x0d, 0x02, 0x01, 0x10, 0x09, 0x01, 0x03, 0x00, 0x00, 0x36, 0x25, 0xc7, 0xd9, 0x60, 0x09, 0x53, 0x45, 0x4c, 0x46, 0x32, 0x00, 0x00, 0x00]
        self.samp_rate = samp_rate = 2000000
        self.freq = freq = 87.5e6
        self.audio_rate = audio_rate = 44100

        ##################################################
        # Blocks
        ##################################################

        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=256,
                decimation=243,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=125,
                decimation=49,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0_0 = filter.rational_resampler_ccc(
                interpolation=100,
                decimation=21,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=50,
                decimation=21,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(40, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.nrsc5_sis_encoder_0 = nrsc5.sis_encoder(mode=nrsc5.pids_mode.FM, short_name='ABCD-FM', slogan='This is ABCD-FM', message='Generated by GNU Radio', program_types=[nrsc5.program_type.NEWS], latitude=40.6892, longitude=(-74.0445), altitude=93.0, country_code='US', fcc_facility_id=0)
        self.nrsc5_psd_encoder_0 = nrsc5.psd_encoder(0, 'Title', 'Artist')
        self.nrsc5_l2_encoder_0 = nrsc5.l2_encoder(1, 0, 146176, 2000)
        self.nrsc5_l1_fm_encoder_mp1_0 = nrsc5.l1_fm_encoder(1)
        self.nrsc5_hdc_encoder_0 = nrsc5.hdc_encoder(2, 64000)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            1,
            firdes.low_pass(
                0.1,
                samp_rate,
                80000,
                20000,
                window.WIN_HAMMING,
                6.76))
        self.fft_vxx_0 = fft.fft_vcc(2048, False, window.rectangular(2048), True, 1)
        self.epy_block_0 = epy_block_0.blk(filename="SLABCD$$010000.png", lot_id=666, port=0x1001)
        self.blocks_wavfile_source_1 = blocks.wavfile_source('sample_mono.wav', True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('sample.wav', True)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 2048)
        self.blocks_vector_source_x_0 = blocks.vector_source_c([math.sin(math.pi / 2 * i / 112) for i in range(112)] + [1] * (2048-112) + [math.cos(math.pi / 2 * i / 112) for i in range(112)], True, 1, [])
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*2048, 2)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.001)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.cons(pmt.make_dict(), pmt.init_u8vector(5 + len(sig), [0x21, 0x20, 0x00, 0x00, 0x00] + sig)), 1000)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 2160, 4096, 0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, (int(audio_rate * 3.5)))
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=audio_rate,
        	quad_rate=(audio_rate * 4),
        	tau=(75e-6),
        	max_dev=75e3,
        	fh=(-1.0),
        )


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.epy_block_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.analog_wfm_tx_0, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.nrsc5_hdc_encoder_0, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.nrsc5_hdc_encoder_0, 1))
        self.connect((self.blocks_wavfile_source_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.nrsc5_hdc_encoder_0, 0), (self.nrsc5_l2_encoder_0, 0))
        self.connect((self.nrsc5_l1_fm_encoder_mp1_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.nrsc5_l2_encoder_0, 0), (self.nrsc5_l1_fm_encoder_mp1_0, 0))
        self.connect((self.nrsc5_psd_encoder_0, 0), (self.nrsc5_l2_encoder_0, 1))
        self.connect((self.nrsc5_sis_encoder_0, 0), (self.nrsc5_l1_fm_encoder_mp1_0, 1))
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.rational_resampler_xxx_0_0_0, 0))
        self.connect((self.rational_resampler_xxx_0_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_sig(self):
        return self.sig

    def set_sig(self, sig):
        self.sig = sig
        self.blocks_message_strobe_0.set_msg(pmt.cons(pmt.make_dict(), pmt.init_u8vector(5 + len(self.sig), [0x21, 0x20, 0x00, 0x00, 0x00] + self.sig)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(0.1, self.samp_rate, 80000, 20000, window.WIN_HAMMING, 6.76))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.blocks_delay_0.set_dly(int((int(self.audio_rate * 3.5))))




def main(top_block_cls=hd_tx_hackrf, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
