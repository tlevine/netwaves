module Main where
 
import           Data.ByteString.Lazy.Char8   (pack)
import qualified Data.ByteString.Lazy         as B
 
header :: Int -> Int -> B.ByteString
header columns rows = pack $ unlines ["P6","32 40","255"]

main :: IO ()
main = do
  contents <- B.readFile "fms_symphony.wav"
  B.putStr $ header 3 2
  B.putStr contents
