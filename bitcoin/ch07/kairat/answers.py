def sig_hash(self, input_index):
    '''Returns the integer representation of the hash that needs to get
    signed for index input_index'''
    # start the serialization with version
    # use int_to_little_endian in 4 bytes
    # add how many inputs there are using encode_varint
    # loop through each input using enumerate, so we have the input index
        # if the input index is the one we're signing
        # the previous tx's ScriptPubkey is the ScriptSig
        # Otherwise, the ScriptSig is empty
        # add the serialization of the input with the ScriptSig we want
    # add how many outputs there are using encode_varint
    # add the serialization of each output
    # add the locktime using int_to_little_endian in 4 bytes
    # add SIGHASH_ALL using int_to_little_endian in 4 bytes
    # hash256 the serialization
    # convert the result to an integer using int.from_bytes(x, 'big')

    s = int_to_little_endian(self.version, 4)
    s += encode_varint(len(self.tx_ins))
    for i, tx_in in enumerate(self.tx_ins):
        if i == input_index:
            s += TxIn(
                prev_tx=tx_in.prev_tx,
                prev_index=tx_in.prev_index,
                script_sig=tx_in.script_pubkey(self.testnet),
                sequence=tx_in.sequence,
            ).serialize()
        else:
            s += TxIn(
                prev_tx=tx_in.prev_tx,
                prev_index=tx_in.prev_index,
                sequence=tx_in.sequence,
            ).serialize()
    s += encode_varint(len(self.tx_outs))
    for tx_out in self.tx_outs:
        s += tx_out.serialize()
    s += int_to_little_endian(self.locktime, 4)
    s += int_to_little_endian(SIGHASH_ALL, 4)
    h256 = hash256(s)
    return int.from_bytes(h256, 'big')


def verify_input(self, input_index):
    '''Returns whether the input has a valid signature'''
    # get the relevant input
    # grab the previous ScriptPubKey
    # get the signature hash (z)
    # combine the current ScriptSig and the previous ScriptPubKey
    # evaluate the combined script
    tx_in = self.tx_ins[input_index]
    script_pubkey = tx_in.script_pubkey(testnet=self.testnet)
    z = self.sig_hash(input_index)
    combined = tx_in.script_sig + script_pubkey
    return combined.evaluate(z)


def sign_input(self, input_index, private_key):
        # get the signature hash (z)
        # get der signature of z from private key
        # append the SIGHASH_ALL to der (use SIGHASH_ALL.to_bytes(1, 'big'))
        # calculate the sec
        # initialize a new script with [sig, sec] as the cmds
        # change input's script_sig to new script
        # return whether sig is valid using self.verify_input
        z = self.sig_hash(input_index)
        der = private_key.sign(z).der()
        sig = der + SIGHASH_ALL.to_bytes(1, 'big')
        sec = private_key.point.sec()
        self.tx_ins[input_index].script_sig = Script([sig, sec])
        return self.verify_input(input_index)