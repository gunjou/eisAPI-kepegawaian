from collections import Counter

from flask import Blueprint, jsonify

from api.query import *

kepegawaian_bp = Blueprint('kepegawaian', __name__)


def count_values(data, param):
    cnt = Counter()
    for i in range(len(data)):
        cnt[data[i][param]] += 1
    return cnt


@kepegawaian_bp.route('/kepegawaian/card_pegawai')
def card_pegawai():
    # Get query result
    result = query_card_pegawai()
    
    # Extract data by date (dict)
    tmp = [{"id": row['IdPegawai'], "jabatan": row['JenisJabatan']} for row in result]

    # Extract data as (dataframe)
    cnts = count_values(tmp, 'jabatan')
    data = [{"name": x, "value": y} for x, y in cnts.items()]
    data.append({"name": "Semua Pegawai", "value": len(tmp)})

    # Define return result as a json
    result = {
        "judul": 'Card Pegawai',
        "label": 'Kepegawaian',
        "data": data, # count_values(data, 'jabatan'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/kepegawaian/kategori_pegawai')
def kategori_pegawai():
    # Get query result
    result = query_kategori_pegawai()

    # Extract data by date (dict)
    tmp = [{"id": row['IdPegawai'], "jenis_pegawai": row['JenisPegawai']} for row in result]

    # Extract data as (dataframe)
    cnts = count_values(tmp, 'jenis_pegawai')
    data = [{"name": x, "value": y} for x, y in cnts.items()]

    # Define return result as a json
    result = {
        "judul": 'Kategori Pegawai',
        "label": 'Kepegawaian',
        "data": data, # count_values(data, 'jenis_pegawai'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/kepegawaian/status_pegawai')
def status_pegawai():
    # Get query result
    result = query_status_pegawai()

    # Extract data by date (dict)
    tmp = [{"id": row['IdPegawai'], "status": row['Status']} for row in result]

    # Extract data as (dataframe)
    cnts = count_values(tmp, 'status')
    data = [{"name": x, "value": y} for x, y in cnts.items()]

    # Define return result as a json
    result = {
        "judul": 'Status Pegawai',
        "label": 'Kepegawaian',
        "data": data, # count_values(data, 'status'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/kepegawaian/pendidikan_jenis_kelamin')
def pendidikan_jenis_kelamin():
    # Get query result
    result = query_pendidikan_jenis_kelamin()

    # Extract data by date (dict)
    tmp = [{"id": row['IdPegawai'], "pendidikan": row['Pendidikan'], "jenis_kelamin": row['JenisKelamin']} for row in result]

    # Extract data as (dataframe)
    cnts = count_values(tmp, 'jenis_kelamin')
    cnts2 = count_values(tmp, 'pendidikan')
    gender = [{"name": x, "value": y} for x, y in cnts.items()]
    education = [{"name": x, "value": y} for x, y in cnts2.items()]
 
    # Define return result as a json
    result = {
        "judul": 'Pendidikan dan Jenis Kelamin',
        "label": 'Kepegawaian',
        "pendidikan": gender,
        "jenis_kelamin": education,
    }
    return jsonify(result)


@kepegawaian_bp.route('/kepegawaian/instalasi_pegawai')
def instalasi_pegawai():
    # Get query result
    result = query_instalasi_pegawai()
    
    # Extract data by date (dict)
    tmp = [{"id": row['IdPegawai'], "instalasi": row['NamaInstalasi']} for row in result]

    # Extract data as (dataframe)
    cnts = count_values(tmp, 'instalasi')
    data = [{"name": x, "value": y} for x, y in cnts.items()]
 
    # Define return result as a json
    result = {
        "judul": 'Instalasi Pegawai',
        "label": 'Kepegawaian',
        "data": data, # count_values(data, 'instalasi'),
    }
    return jsonify(result)
