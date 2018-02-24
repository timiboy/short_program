// 从网站JS中复制出来的部分
function BigInteger(t, r, n) {
    null != t && ("number" == typeof t ? this.fromNumber(t, r, n) : null == r && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, r))
}

function nbi() {
    return new BigInteger(null)
}

function am1(t, r, n, i, e, o) {
    for (; --o >= 0;) {
        var s = r * this[t++] + n[i] + e;
        e = Math.floor(s / 67108864), n[i++] = 67108863 & s
    }
    return e
}

function am2(t, r, n, i, e, o) {
    for (var s = 32767 & r, h = r >> 15; --o >= 0;) {
        var p = 32767 & this[t],
            a = this[t++] >> 15,
            u = h * p + a * s;
        p = s * p + ((32767 & u) << 15) + n[i] + (1073741823 & e), e = (p >>> 30) + (u >>> 15) + h * a + (e >>> 30), n[i++] = 1073741823 & p
    }
    return e
}

function am3(t, r, n, i, e, o) {
    for (var s = 16383 & r, h = r >> 14; --o >= 0;) {
        var p = 16383 & this[t],
            a = this[t++] >> 14,
            u = h * p + a * s;
        p = s * p + ((16383 & u) << 14) + n[i] + e, e = (p >> 28) + (u >> 14) + h * a, n[i++] = 268435455 & p
    }
    return e
}

function int2char(t) {
    return BI_RM.charAt(t)
}

function intAt(t, r) {
    var n = BI_RC[t.charCodeAt(r)];
    return null == n ? -1 : n
}

function bnpCopyTo(t) {
    for (var r = this.t - 1; r >= 0; --r) t[r] = this[r];
    t.t = this.t, t.s = this.s
}

function bnpFromInt(t) {
    this.t = 1, this.s = t < 0 ? -1 : 0, t > 0 ? this[0] = t : t < -1 ? this[0] = t + DV : this.t = 0
}

function nbv(t) {
    var r = nbi();
    return r.fromInt(t), r
}

function bnpFromString(t, r) {
    var n;
    if (16 == r) n = 4;
    else if (8 == r) n = 3;
    else if (256 == r) n = 8;
    else if (2 == r) n = 1;
    else if (32 == r) n = 5;
    else {
        if (4 != r) return void this.fromRadix(t, r);
        n = 2
    }
    this.t = 0, this.s = 0;
    for (var i = t.length, e = !1, o = 0; --i >= 0;) {
        var s = 8 == n ? 255 & t[i] : intAt(t, i);
        s < 0 ? "-" == t.charAt(i) && (e = !0) : (e = !1, 0 == o ? this[this.t++] = s : o + n > this.DB ? (this[this.t - 1] |= (s & (1 << this.DB - o) - 1) << o, this[this.t++] = s >> this.DB - o) : this[this.t - 1] |= s << o, o += n, o >= this.DB && (o -= this.DB))
    }
    8 == n && 0 != (128 & t[0]) && (this.s = -1, o > 0 && (this[this.t - 1] |= (1 << this.DB - o) - 1 << o)), this.clamp(), e && BigInteger.ZERO.subTo(this, this)
}

function bnpClamp() {
    for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t;)--this.t
}

function bnToString(t) {
    if (this.s < 0) return "-" + this.negate().toString(t);
    var r;
    if (16 == t) r = 4;
    else if (8 == t) r = 3;
    else if (2 == t) r = 1;
    else if (32 == t) r = 5;
    else {
        if (4 != t) return this.toRadix(t);
        r = 2
    }
    var n, i = (1 << r) - 1,
        e = !1,
        o = "",
        s = this.t,
        h = this.DB - s * this.DB % r;
    if (s-- > 0)
        for (h < this.DB && (n = this[s] >> h) > 0 && (e = !0, o = int2char(n)); s >= 0;) h < r ? (n = (this[s] & (1 << h) - 1) << r - h, n |= this[--s] >> (h += this.DB - r)) : (n = this[s] >> (h -= r) & i, h <= 0 && (h += this.DB, --s)), n > 0 && (e = !0), e && (o += int2char(n));
    return e ? o : "0"
}

function bnNegate() {
    var t = nbi();
    return BigInteger.ZERO.subTo(this, t), t
}

function bnAbs() {
    return this.s < 0 ? this.negate() : this
}

function bnCompareTo(t) {
    var r = this.s - t.s;
    if (0 != r) return r;
    var n = this.t;
    if (r = n - t.t, 0 != r) return r;
    for (; --n >= 0;)
        if (0 != (r = this[n] - t[n])) return r;
    return 0
}

function nbits(t) {
    var r, n = 1;
    return 0 != (r = t >>> 16) && (t = r, n += 16), 0 != (r = t >> 8) && (t = r, n += 8), 0 != (r = t >> 4) && (t = r, n += 4), 0 != (r = t >> 2) && (t = r, n += 2), 0 != (r = t >> 1) && (t = r, n += 1), n
}

function bnBitLength() {
    return this.t <= 0 ? 0 : this.DB * (this.t - 1) + nbits(this[this.t - 1] ^ this.s & this.DM)
}

function bnpDLShiftTo(t, r) {
    var n;
    for (n = this.t - 1; n >= 0; --n) r[n + t] = this[n];
    for (n = t - 1; n >= 0; --n) r[n] = 0;
    r.t = this.t + t, r.s = this.s
}

function bnpDRShiftTo(t, r) {
    for (var n = t; n < this.t; ++n) r[n - t] = this[n];
    r.t = Math.max(this.t - t, 0), r.s = this.s
}

function bnpLShiftTo(t, r) {
    var n, i = t % this.DB,
        e = this.DB - i,
        o = (1 << e) - 1,
        s = Math.floor(t / this.DB),
        h = this.s << i & this.DM;
    for (n = this.t - 1; n >= 0; --n) r[n + s + 1] = this[n] >> e | h, h = (this[n] & o) << i;
    for (n = s - 1; n >= 0; --n) r[n] = 0;
    r[s] = h, r.t = this.t + s + 1, r.s = this.s, r.clamp()
}

function bnpRShiftTo(t, r) {
    r.s = this.s;
    var n = Math.floor(t / this.DB);
    if (n >= this.t) return void(r.t = 0);
    var i = t % this.DB,
        e = this.DB - i,
        o = (1 << i) - 1;
    r[0] = this[n] >> i;
    for (var s = n + 1; s < this.t; ++s) r[s - n - 1] |= (this[s] & o) << e, r[s - n] = this[s] >> i;
    i > 0 && (r[this.t - n - 1] |= (this.s & o) << e), r.t = this.t - n, r.clamp()
}

function bnpSubTo(t, r) {
    for (var n = 0, i = 0, e = Math.min(t.t, this.t); n < e;) i += this[n] - t[n], r[n++] = i & this.DM, i >>= this.DB;
    if (t.t < this.t) {
        for (i -= t.s; n < this.t;) i += this[n], r[n++] = i & this.DM, i >>= this.DB;
        i += this.s
    } else {
        for (i += this.s; n < t.t;) i -= t[n], r[n++] = i & this.DM, i >>= this.DB;
        i -= t.s
    }
    r.s = i < 0 ? -1 : 0, i < -1 ? r[n++] = this.DV + i : i > 0 && (r[n++] = i), r.t = n, r.clamp()
}

function bnpMultiplyTo(t, r) {
    var n = this.abs(),
        i = t.abs(),
        e = n.t;
    for (r.t = e + i.t; --e >= 0;) r[e] = 0;
    for (e = 0; e < i.t; ++e) r[e + n.t] = n.am(0, i[e], r, e, 0, n.t);
    r.s = 0, r.clamp(), this.s != t.s && BigInteger.ZERO.subTo(r, r)
}

function bnpSquareTo(t) {
    for (var r = this.abs(), n = t.t = 2 * r.t; --n >= 0;) t[n] = 0;
    for (n = 0; n < r.t - 1; ++n) {
        var i = r.am(n, r[n], t, 2 * n, 0, 1);
        (t[n + r.t] += r.am(n + 1, 2 * r[n], t, 2 * n + 1, i, r.t - n - 1)) >= r.DV && (t[n + r.t] -= r.DV, t[n + r.t + 1] = 1)
    }
    t.t > 0 && (t[t.t - 1] += r.am(n, r[n], t, 2 * n, 0, 1)), t.s = 0, t.clamp()
}

function bnpDivRemTo(t, r, n) {
    var i = t.abs();
    if (!(i.t <= 0)) {
        var e = this.abs();
        if (e.t < i.t) return null != r && r.fromInt(0), void(null != n && this.copyTo(n));
        null == n && (n = nbi());
        var o = nbi(),
            s = this.s,
            h = t.s,
            p = this.DB - nbits(i[i.t - 1]);
        p > 0 ? (i.lShiftTo(p, o), e.lShiftTo(p, n)) : (i.copyTo(o), e.copyTo(n));
        var a = o.t,
            u = o[a - 1];
        if (0 != u) {
            var g = u * (1 << this.F1) + (a > 1 ? o[a - 2] >> this.F2 : 0),
                f = this.FV / g,
                c = (1 << this.F1) / g,
                l = 1 << this.F2,
                v = n.t,
                b = v - a,
                m = null == r ? nbi() : r;
            for (o.dlShiftTo(b, m), n.compareTo(m) >= 0 && (n[n.t++] = 1, n.subTo(m, n)), BigInteger.ONE.dlShiftTo(a, m), m.subTo(o, o); o.t < a;) o[o.t++] = 0;
            for (; --b >= 0;) {
                var B = n[--v] == u ? this.DM : Math.floor(n[v] * f + (n[v - 1] + l) * c);
                if ((n[v] += o.am(0, B, n, b, 0, a)) < B)
                    for (o.dlShiftTo(b, m), n.subTo(m, n); n[v] < --B;) n.subTo(m, n)
            }
            null != r && (n.drShiftTo(a, r), s != h && BigInteger.ZERO.subTo(r, r)), n.t = a, n.clamp(), p > 0 && n.rShiftTo(p, n), s < 0 && BigInteger.ZERO.subTo(n, n)
        }
    }
}

function bnMod(t) {
    var r = nbi();
    return this.abs().divRemTo(t, null, r), this.s < 0 && r.compareTo(BigInteger.ZERO) > 0 && t.subTo(r, r), r
}

function Classic(t) {
    this.m = t
}

function cConvert(t) {
    return t.s < 0 || t.compareTo(this.m) >= 0 ? t.mod(this.m) : t
}

function cRevert(t) {
    return t
}

function cReduce(t) {
    t.divRemTo(this.m, null, t)
}

function cMulTo(t, r, n) {
    t.multiplyTo(r, n), this.reduce(n)
}

function cSqrTo(t, r) {
    t.squareTo(r), this.reduce(r)
}

function bnpInvDigit() {
    if (this.t < 1) return 0;
    var t = this[0];
    if (0 == (1 & t)) return 0;
    var r = 3 & t;
    return r = r * (2 - (15 & t) * r) & 15, r = r * (2 - (255 & t) * r) & 255, r = r * (2 - ((65535 & t) * r & 65535)) & 65535, r = r * (2 - t * r % this.DV) % this.DV, r > 0 ? this.DV - r : -r
}

function Montgomery(t) {
    this.m = t, this.mp = t.invDigit(), this.mpl = 32767 & this.mp, this.mph = this.mp >> 15, this.um = (1 << t.DB - 15) - 1, this.mt2 = 2 * t.t
}

function montConvert(t) {
    var r = nbi();
    return t.abs().dlShiftTo(this.m.t, r), r.divRemTo(this.m, null, r), t.s < 0 && r.compareTo(BigInteger.ZERO) > 0 && this.m.subTo(r, r), r
}

function montRevert(t) {
    var r = nbi();
    return t.copyTo(r), this.reduce(r), r
}

function montReduce(t) {
    for (; t.t <= this.mt2;) t[t.t++] = 0;
    for (var r = 0; r < this.m.t; ++r) {
        var n = 32767 & t[r],
            i = n * this.mpl + ((n * this.mph + (t[r] >> 15) * this.mpl & this.um) << 15) & t.DM;
        for (n = r + this.m.t, t[n] += this.m.am(0, i, t, r, 0, this.m.t); t[n] >= t.DV;) t[n] -= t.DV, t[++n]++
    }
    t.clamp(), t.drShiftTo(this.m.t, t), t.compareTo(this.m) >= 0 && t.subTo(this.m, t)
}

function montSqrTo(t, r) {
    t.squareTo(r), this.reduce(r)
}

function montMulTo(t, r, n) {
    t.multiplyTo(r, n), this.reduce(n)
}

function bnpIsEven() {
    return 0 == (this.t > 0 ? 1 & this[0] : this.s)
}

function bnpExp(t, r) {
    if (t > 4294967295 || t < 1) return BigInteger.ONE;
    var n = nbi(),
        i = nbi(),
        e = r.convert(this),
        o = nbits(t) - 1;
    for (e.copyTo(n); --o >= 0;)
        if (r.sqrTo(n, i), (t & 1 << o) > 0) r.mulTo(i, e, n);
        else {
            var s = n;
            n = i, i = s
        }
    return r.revert(n)
}

function bnModPowInt(t, r) {
    var n;
    return n = t < 256 || r.isEven() ? new Classic(r) : new Montgomery(r), this.exp(t, n)
}

function Arcfour() {
    this.i = 0, this.j = 0, this.S = new Array
}

function ARC4init(t) {
    var r, n, i;
    for (r = 0; r < 256; ++r) this.S[r] = r;
    for (n = 0, r = 0; r < 256; ++r) n = n + this.S[r] + t[r % t.length] & 255, i = this.S[r], this.S[r] = this.S[n], this.S[n] = i;
    this.i = 0, this.j = 0
}

function ARC4next() {
    var t;
    return this.i = this.i + 1 & 255, this.j = this.j + this.S[this.i] & 255, t = this.S[this.i], this.S[this.i] = this.S[this.j], this.S[this.j] = t, this.S[t + this.S[this.i] & 255]
}

function prng_newstate() {
    return new Arcfour
}

function rng_seed_int(t) {
    rng_pool[rng_pptr++] ^= 255 & t, rng_pool[rng_pptr++] ^= t >> 8 & 255, rng_pool[rng_pptr++] ^= t >> 16 & 255, rng_pool[rng_pptr++] ^= t >> 24 & 255, rng_pptr >= rng_psize && (rng_pptr -= rng_psize)
}

function rng_seed_time() {
    rng_seed_int((new Date).getTime())
}

function rng_get_byte() {
    if (null == rng_state) {
        for (rng_seed_time(), rng_state = prng_newstate(), rng_state.init(rng_pool), rng_pptr = 0; rng_pptr < rng_pool.length; ++rng_pptr) rng_pool[rng_pptr] = 0;
        rng_pptr = 0
    }
    return rng_state.next()
}

function rng_get_bytes(t) {
    var r;
    for (r = 0; r < t.length; ++r) t[r] = rng_get_byte()
}

function SecureRandom() {}

function parseBigInt(t, r) {
    return new BigInteger(t, r)
}

function linebrk(t, r) {
    for (var n = "", i = 0; i + r < t.length;) n += t.substring(i, i + r) + "\n", i += r;
    return n + t.substring(i, t.length)
}

function byte2Hex(t) {
    return t < 16 ? "0" + t.toString(16) : t.toString(16)
}

function pkcs1pad2(t, r) {
    if (r < t.length + 2) return alert("密码太长!"), null;
    var n = new Array,
        i = t.length - 1,
        e = t.length;
    if (!(e < 100)) return alert("密码太长!"), null;
    n[0] = 48 + e / 10, n[1] = 48 + e % 10;
    var o = 2;
    for (i = 0; i < e && r > 0;) n[o++] = t.charCodeAt(i++);
    for (var s = new SecureRandom, h = new Array; o < r;) {
        for (h[0] = 0; 0 == h[0];) s.nextBytes(h);
        n[o++] = h[0]
    }
    return new BigInteger(n)
}

function RSAKey() {
    this.n = null, this.e = 0, this.d = null, this.p = null, this.q = null, this.dmp1 = null, this.dmq1 = null, this.coeff = null
}

function RSASetPublic(t, r) {
    null != t && null != r && t.length > 0 && r.length > 0 ? (this.n = parseBigInt(t, 16), this.e = parseInt(r, 16)) : alert("Invalid RSA public key")
}

function RSADoPublic(t) {
    return t.modPowInt(this.e, this.n)
}

function RSAEncrypt(t) {
    var r = pkcs1pad2(t, this.n.bitLength() + 7 >> 3);
    if (null == r) return null;
    var n = this.doPublic(r);
    if (null == n) return null;
    for (var i = n.toString(16).toUpperCase(), e = 256 - i.length, o = 0; o < e; o += 1) i = "0" + i;
    return i
}

function hex2b64(t) {
    var r, n, i = "";
    for (r = 0; r + 3 <= t.length; r += 3) n = parseInt(t.substring(r, r + 3), 16), i += b64map.charAt(n >> 6) + b64map.charAt(63 & n);
    for (r + 1 == t.length ? (n = parseInt(t.substring(r, r + 1), 16), i += b64map.charAt(n << 2)) : r + 2 == t.length && (n = parseInt(t.substring(r, r + 2), 16), i += b64map.charAt(n >> 2) + b64map.charAt((3 & n) << 4));
        (3 & i.length) > 0;) i += b64pad;
    return i
}

function b64tohex(t) {
    var r, n, i = "",
        e = 0;
    for (r = 0; r < t.length && t.charAt(r) != b64pad; ++r) v = b64map.indexOf(t.charAt(r)), v < 0 || (0 == e ? (i += int2char(v >> 2), n = 3 & v, e = 1) : 1 == e ? (i += int2char(n << 2 | v >> 4), n = 15 & v, e = 2) : 2 == e ? (i += int2char(n), i += int2char(v >> 2), n = 3 & v, e = 3) : (i += int2char(n << 2 | v >> 4), i += int2char(15 & v), e = 0));
    return 1 == e && (i += int2char(n << 2)), i
}

function b64toBA(t) {
    var r, n = b64tohex(t),
        i = new Array;
    for (r = 0; 2 * r < n.length; ++r) i[r] = parseInt(n.substring(2 * r, 2 * r + 2), 16);
    return i
}

function liuhjtest() {
    var t = "B1204FC8EB406948947F0F69E460BFEA19E778D7D3619AFE3EBEF3CEACA10A289F303E3EA717850757B43948FC3C6AE766B4AA8A08F927F976A0313DCB6054860DFF1CDE7DF5C87E2E3147CC9DCDDF31C97282B975088DF94679A4F1E53EFEBF68FC3717D28D00E51BED299CB1815777265B0DB4576CC314C82612277626F82D",
        r = new RSAKey;
    r.setPublic(t, "10001");
    var n = r.encrypt("1234567890abcdefghijklmnopqrstuvwxyz<>?,./:;'{}[]!@#$%^&*_+|=-");
    document.getElementById("txt1").value = n
}
var dbits, canary = 0xdeadbeefcafe,
    j_lm = 15715070 == (16777215 & canary);
j_lm && "Microsoft Internet Explorer" == navigator.appName ? (BigInteger.prototype.am = am2, dbits = 30) : j_lm && "Netscape" != navigator.appName ? (BigInteger.prototype.am = am1, dbits = 26) : (BigInteger.prototype.am = am3, dbits = 28), BigInteger.prototype.DB = dbits, BigInteger.prototype.DM = (1 << dbits) - 1, BigInteger.prototype.DV = 1 << dbits;
var BI_FP = 52;
BigInteger.prototype.FV = Math.pow(2, BI_FP), BigInteger.prototype.F1 = BI_FP - dbits, BigInteger.prototype.F2 = 2 * dbits - BI_FP;
var BI_RM = "0123456789abcdefghijklmnopqrstuvwxyz",
    BI_RC = new Array,
    rr, vv;
for (rr = "0".charCodeAt(0), vv = 0; vv <= 9; ++vv) BI_RC[rr++] = vv;
for (rr = "a".charCodeAt(0), vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
for (rr = "A".charCodeAt(0), vv = 10; vv < 36; ++vv) BI_RC[rr++] = vv;
Classic.prototype.convert = cConvert, Classic.prototype.revert = cRevert, Classic.prototype.reduce = cReduce, Classic.prototype.mulTo = cMulTo, Classic.prototype.sqrTo = cSqrTo, Montgomery.prototype.convert = montConvert, Montgomery.prototype.revert = montRevert, Montgomery.prototype.reduce = montReduce, Montgomery.prototype.mulTo = montMulTo, Montgomery.prototype.sqrTo = montSqrTo, BigInteger.prototype.copyTo = bnpCopyTo, BigInteger.prototype.fromInt = bnpFromInt, BigInteger.prototype.fromString = bnpFromString, BigInteger.prototype.clamp = bnpClamp, BigInteger.prototype.dlShiftTo = bnpDLShiftTo, BigInteger.prototype.drShiftTo = bnpDRShiftTo, BigInteger.prototype.lShiftTo = bnpLShiftTo, BigInteger.prototype.rShiftTo = bnpRShiftTo, BigInteger.prototype.subTo = bnpSubTo, BigInteger.prototype.multiplyTo = bnpMultiplyTo, BigInteger.prototype.squareTo = bnpSquareTo, BigInteger.prototype.divRemTo = bnpDivRemTo, BigInteger.prototype.invDigit = bnpInvDigit, BigInteger.prototype.isEven = bnpIsEven, BigInteger.prototype.exp = bnpExp, BigInteger.prototype.toString = bnToString, BigInteger.prototype.negate = bnNegate, BigInteger.prototype.abs = bnAbs, BigInteger.prototype.compareTo = bnCompareTo, BigInteger.prototype.bitLength = bnBitLength, BigInteger.prototype.mod = bnMod, BigInteger.prototype.modPowInt = bnModPowInt, BigInteger.ZERO = nbv(0), BigInteger.ONE = nbv(1), Arcfour.prototype.init = ARC4init, Arcfour.prototype.next = ARC4next;
var rng_psize = 256,
    rng_state, rng_pool, rng_pptr;
if (null == rng_pool) {
    rng_pool = new Array, rng_pptr = 0;
    var t;
    if ("Netscape" == navigator.appName && navigator.appVersion < "5" && window.crypto) {
        var z = window.crypto.random(32);
        for (t = 0; t < z.length; ++t) rng_pool[rng_pptr++] = 255 & z.charCodeAt(t)
    }
    for (; rng_pptr < rng_psize;) t = Math.floor(65536 * Math.random()), rng_pool[rng_pptr++] = t >>> 8, rng_pool[rng_pptr++] = 255 & t;
    rng_pptr = 0, rng_seed_time()
}
SecureRandom.prototype.nextBytes = rng_get_bytes, RSAKey.prototype.doPublic = RSADoPublic, RSAKey.prototype.setPublic = RSASetPublic, RSAKey.prototype.encrypt = RSAEncrypt;
var b64map = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
    b64pad = "=";

// 添加加密函数
function run(pwd){
    public = 'BE24E372DC1B329633A6A014A7C02797915E3C363DD6EE119377BD645329B7E6446B4A71AC5F878EBC870C6D8BFD3C06B92E6C6E93390B34192A7A9E430800091761473FAC2CC0A68A828B2589A8CB729C19161E8E27F4C0F3CDE9701FAFE48D2B65947799072AFA6A3F2D7BDBEF8B6D7429C2D115A3E5F723467D57B3AC6967';
    exp = '10001';
    var a = new RSAKey;
    a.setPublic(public, exp);
    var e = a.encrypt(pwd);
    return e
}