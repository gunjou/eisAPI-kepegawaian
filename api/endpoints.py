from collections import Counter
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from flask import Blueprint, jsonify, request
from sqlalchemy import text

from api.config import MONTH_ID as month_id
from api.config import get_connection

kepegawaian_bp = Blueprint('kepegawaian', __name__)
engine = get_connection()


def get_default_date(tgl_awal, tgl_akhir):
    if tgl_awal == None:
        tgl_awal = datetime.today() - relativedelta(months=1)
        tgl_awal = datetime.strptime(tgl_awal.strftime('%Y-%m-%d'), '%Y-%m-%d')
    else:
        tgl_awal = datetime.strptime(tgl_awal, '%Y-%m-%d')

    if tgl_akhir == None:
        tgl_akhir = datetime.strptime(
            datetime.today().strftime('%Y-%m-%d'), '%Y-%m-%d')
    else:
        tgl_akhir = datetime.strptime(tgl_akhir, '%Y-%m-%d')
    return tgl_awal, tgl_akhir


@kepegawaian_bp.route('/card_pegawai')
def card_pegawai():
    return jsonify({"message": "ini data card kepegawaian"})


@kepegawaian_bp.route('/kategori_pegawai')
def kategori_pegawai():
    return jsonify({"message": "ini data kategori pegawai"})


@kepegawaian_bp.route('/status_pegawai')
def status_pegawai():
    return jsonify({"message": "ini data status_pegawai"})


@kepegawaian_bp.route('/pendidikan_jenis_kelamin')
def pendidikan_jenis_kelamin():
    return jsonify({"message": "ini data pendidikan dan jenis kelamin"})


@kepegawaian_bp.route('/instalasi_pegawai')
def instalasi_pegawai():
    return jsonify({"message": "ini data instalasi pegawai"})
