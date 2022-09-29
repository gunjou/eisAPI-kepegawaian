from collections import Counter

from flask import Blueprint, jsonify
from sqlalchemy import text

from api.config import get_connection

kepegawaian_bp = Blueprint('kepegawaian', __name__)
engine = get_connection()


def count_values(data, param):
    cnt = Counter()
    for i in range(len(data)):
        cnt[data[i][param].lower().replace(' ', '_')] += 1
    return cnt


@kepegawaian_bp.route('/card_pegawai')
def card_pegawai():
    result = engine.execute(
        text(
            f"""SELECT dcp.IdPegawai, jj.JenisJabatan  
			 FROM dbo.DataCurrentPegawai dcp
			 INNER JOIN dbo.Jabatan j 
			 ON dcp.KdJabatan = j.KdJabatan 
			 INNER JOIN dbo.JenisJabatan jj 
			 ON j.KdJenisJabatan = jj.KdJenisJabatan 
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    data = []
    for row in result:
        data.append({
            "id": row['IdPegawai'],
            "jabatan": row['JenisJabatan'],
            "judul": 'Card Pegawai',
            "label": 'Kepegawaian'
        })

    result = {
        "judul": 'Card Pegawai',
        "label": 'Kepegawaian',
        "card": count_values(data, 'jabatan'),
    }
    result['card']['semua_pegawai'] = len(data)
    return jsonify(result)


@kepegawaian_bp.route('/kategori_pegawai')
def kategori_pegawai():
    result = engine.execute(
        text(
            f"""SELECT dp.IdPegawai, jp.JenisPegawai 
			 FROM dbo.DataPegawai dp
			 INNER JOIN dbo.JenisPegawai jp
			 ON dp.KdJenisPegawai = jp.KdJenisPegawai
             WHERE dp.IdPegawai <> '8888888888'
           	 ORDER BY dp.IdPegawai ASC;"""))
    data = []
    for row in result:
        data.append({
            "id": row['IdPegawai'],
            "jenis_pegawai": row['JenisPegawai'],
            "judul": 'Kategori Pegawai',
            "label": 'Kepegawaian'
        })

    result = {
        "judul": 'Kategori Pegawai',
        "label": 'Kepegawaian',
        "kategori": count_values(data, 'jenis_pegawai'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/status_pegawai')
def status_pegawai():
    result = engine.execute(
        text(
            f"""SELECT dcp.IdPegawai, sp.Status 
			 FROM dbo.DataCurrentPegawai dcp 
			 INNER JOIN dbo.StatusPegawai sp 
			 ON dcp.KdStatus = sp.KdStatus
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    data = []
    for row in result:
        data.append({
            "id": row['IdPegawai'],
            "status": row['Status'],
            "judul": 'Status Pegawai',
            "label": 'Kepegawaian'
        })

    result = {
        "judul": 'Status Pegawai',
        "label": 'Kepegawaian',
        "kategori": count_values(data, 'status'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/pendidikan_jenis_kelamin')
def pendidikan_jenis_kelamin():
    result = engine.execute(
        text(
            f"""SELECT dcp.IdPegawai, p.Pendidikan, dp.JenisKelamin  
			FROM dbo.DataCurrentPegawai dcp 
			INNER JOIN dbo.DataPegawai dp 
			ON dcp.IdPegawai = dp.IdPegawai
			INNER JOIN dbo.KualifikasiJurusan kj  
			ON dcp.KdKualifikasiJurusan = kj.KdKualifikasiJurusan 
			INNER JOIN dbo.Pendidikan p  
			ON kj.KdPendidikan = p.KdPendidikan 
			WHERE dcp.IdPegawai <> '8888888888'
           	ORDER BY dcp.IdPegawai ASC;"""))
    data = []
    for row in result:
        data.append({
            "id": row['IdPegawai'],
            "pendidikan": row['Pendidikan'],
            "jenis_kelamin": row['JenisKelamin'],
            "judul": 'Pendidikan dan Jenis Kelamin',
            "label": 'Kepegawaian'
        })

    result = {
        "judul": 'Pendidikan dan Jenis Kelamin',
        "label": 'Kepegawaian',
        "pendidikan": count_values(data, 'pendidikan'),
        "jenis_kelamin": count_values(data, 'jenis_kelamin'),
    }
    return jsonify(result)


@kepegawaian_bp.route('/instalasi_pegawai')
def instalasi_pegawai():
    result = engine.execute(
        text(
            f"""SELECT dcp.IdPegawai, i.NamaInstalasi  
			 FROM dbo.DataCurrentPegawai dcp
			 INNER JOIN dbo.Ruangan r  
			 ON dcp.KdRuanganKerja = r.KdRuangan 
			 INNER JOIN dbo.Instalasi i  
			 ON r.KdInstalasi = i.KdInstalasi  
			 WHERE dcp.IdPegawai <> '8888888888'
           	 ORDER BY dcp.IdPegawai ASC;"""))
    data = []
    for row in result:
        data.append({
            "id": row['IdPegawai'],
            "instalasi": row['NamaInstalasi'],
            "judul": 'Instalasi Pegawai',
            "label": 'Kepegawaian'
        })

    result = {
        "judul": 'Pendidikan dan Jenis Kelamin',
        "label": 'Kepegawaian',
        "instalasi": count_values(data, 'instalasi'),
    }
    return jsonify(result)
